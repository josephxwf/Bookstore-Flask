from flask import render_template
from coreapp import app
from flask import url_for # used for redirect to another page see home.html
import re
from bs4 import BeautifulSoup
#from sortedcontainers import SortedDict
def get_chap_links(page):
	soup = BeautifulSoup(page)
	links = [str(link.get('name')) for link in soup.find_all('a') if not link.get('href')]# last if condition filters only links that not begin with href
	return links


def parse_wizofoz(bookname):
    page = render_template(bookname) # render back to web page
    links = get_chap_links(page) # use the function above to extract link in the wizofoz.html page
    sections = []
	# get each section from wizofoz.html and put into sections dictionary.
    for ind in range(len(links)):

        section = {}
        start = links[ind]
        if ind < len(links) - 1:
            end = links[ind + 1]
			# pattern for getting each section by extracting content between two sections
            patt = ('<a name="{}"(.*)' + '<a name="{}"').format(start,end)
            match = re.search(patt, page, re.MULTILINE | re.DOTALL)

        else:
            patt = '<a name="{}"(.*)'.format(start)
            match = re.search(patt, page, re.MULTILINE | re.DOTALL)
        if match:
            soup = BeautifulSoup(match.group(1))
            plist = [p.contents[0] for p in soup.find_all('p') if p.contents]
            #section['title'] = soup.find('h3').contents[0]
            section['title'] = start
            section['order'] = ind  # order and label each dictionary
            section['plist'] = plist
            sections.append(section)
    return links, sections

@app.route('/')
def home():
  data = {'image_url1':'/static/wonderfulWizard.jpg','image_url2':'/static/lostPrincess.jpg'}
  #data['anchor'] = SortedDict(parse_wizofoz()[1])
  data['anchor'] = parse_wizofoz('wizofoz.html')[1]
  #page = render_template('wizofoz.html')
  #data1 = {'links':get_chap_links(page), 'y':parse_wizofoz()}
  return render_template('home.html', **data)
  #return render_template('home.html', **data1)


@app.route('/ebook1')
def ebook1():
  data = {'title':'The Wonderful Wizard of Oz','image_url':'/static/wonderfulWizard.jpg'}
  #data['anchor'] = SortedDict(parse_wizofoz()[1])
  data['anchor'] = parse_wizofoz('wizofoz.html')[1]
  data['source']= 'wizofoz.html'
  #page = render_template('wizofoz.html')
  #data1 = {'links':get_chap_links(page), 'y':parse_wizofoz()}
  return render_template('ebook1.html', **data)

@app.route('/ebook2')
def ebook2():
   data = {'title':'The Lost Princess of Oz','image_url':'/static/lostPrincess.jpg'}
   #data['anchor'] = SortedDict(parse_wizofoz()[1])
   data['anchor'] = parse_wizofoz('lostprincess.html')[1]
   #page = render_template('wizofoz.html')
   #data1 = {'links':get_chap_links(page), 'y':parse_wizofoz()}
   data['source']= 'lostprincess.html'
   return render_template('ebook2.html', **data)


# dreirect depends on the section num and the name of book in html .
@app.route('/<int:num><source>') # source identify the book name, num indentify the chapter
def section(num,source):
  data = {'title':'The Wonderful Wizard of Oz','image_url':'/static/title_img.jpg'}
  data['anchor'] = parse_wizofoz(source)[1]
  data['dic'] = parse_wizofoz(source)[1][num]#get the specific dictionary that contains that chapter label by num
  data['source']= source

  return render_template('section.html',**data)
