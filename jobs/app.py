import Flask
from flask import render_template


app == Flask(__name__)

@route('/')
@route('jobs')
def jobs():
    return render_template('index.html')
