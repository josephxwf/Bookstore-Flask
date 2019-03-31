# used to local test your code by command python main.py
from flask import Flask
from coreapp import app

app.debug = True
if __name__ == '__main__':
    app.run()