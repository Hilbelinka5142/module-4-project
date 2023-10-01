#from requests import get

#ip = get('https://api.ipify.org').text
#print('My public IP address is: {}'.format(ip))

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
