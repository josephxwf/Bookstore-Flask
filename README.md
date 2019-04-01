# Bookstore-Flask


Simple online bookstore that was developed with Flask.


## Prerequisites


* Pyhton 2.7



## Installation

* Install pip
  * `easy_install pip`
  
* Install virtual environment
  * ` pip install --user virtualenv`
  
* Create Virtualenv
  * `virtualenv ENV`
  
* Activtate Virtualenv 
    * `source /path/to/ENV/bin/activate`
    
* install flask
    * `pip install Flask`
        

## Development set up and run the app

1. Method 1 to run flask app
   * cd to root directory
   * `python main.py`
   * Now head over to http://127.0.0.1:5000/, and you should see the online bookstore

2. Method 2 to run flask app
   * cd to root directory
   * ` export FLASK_APP=my_application`
   *  `export FLASK_ENV=development`
   *  `flask run`


## Issues

1. oserror: [errno 98] address already in use flask:
   * `ps -fA | grep python`
   * You will get a pid number by naming of your flask number. Now copy the pid number from second column of your project row of terminal output.
   
   * `kill -9 pid` The terminal will restart and then run the command below
   * `flask run`

## Authors

* **Joseph Fan** - *init work* - [josephxwf](https://github.com/josephxwf)



