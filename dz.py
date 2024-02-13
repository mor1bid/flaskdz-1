from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

prog = Flask(__name__)

@prog.route('/')
def wares():
    return render_template('index.html')

@prog.route('/boots/')
def boots():
    return render_template('boots.html')

@prog.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@prog.route('/curtco/')
def curtco():
    return render_template('curtcobain.html')

if __name__=="__main__":
    prog.run()