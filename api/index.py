from requests import get, template

app = get(__name__)

@app.route('/')
def home():
    ip = get('https://api.ipify.org').text
    data = print('My public IP address is: {}'.format(ip))
    return template('index.html', data)

@app.route('/about')
def about():
    return 'about'
    
