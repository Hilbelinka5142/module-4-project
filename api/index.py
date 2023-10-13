from flask import Flask, request
from request import get

app = get(__name__)

@app.route('/')
def home():
    ip = requests.get('https://api.ipify.org').text
    data = 'My public IP address is: {}'.format(ip)
    return print('index.html', data)

@app.route('/about')
def about():
    return 'about'
