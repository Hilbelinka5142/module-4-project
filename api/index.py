<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    className = 'cnit 381'

    return render_template('index.html', data=className)

@app.route('/about')
def about():
    return 'About'

@app.route('/another')
def another():
    return 'Another'
=======
from requests import get


app = get(__name__)

@app.route('/')
def home():
    ip = get('https://api.ipify.org').text
    return ('My public IP address is: {}'.format(ip))



>>>>>>> aa434fc333687aa2070aebbc7b286d272665fd4b
