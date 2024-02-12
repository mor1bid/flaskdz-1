from flask import Flask, render_template

prog = Flask(__name__)

@prog.route('/')
def wares():
    return render_template('index.html')

if __name__=="__main__":
    prog.run()