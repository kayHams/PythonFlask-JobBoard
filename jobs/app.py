from flask import render_template, Flask


app == Flask(__name__)

@route('/')
@route('jobs')
def jobs():
    return render_template('index.html')
