from flask import Flask, render_template
from requests import get

app = Flask(__name__)

@app.route('/')
def home():
    ip = requests.get('https://api.ipify.org').text
    data = 'My public IP address is: {}'.format(ip)
    return print('index.html', data)

@app.route('/about')
def about():
    return 'About'

@app.route('/another')
def another():
    return 'Another'
