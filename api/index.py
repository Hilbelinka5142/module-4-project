from requests import get


app = get(__name__)

@app.route('/')
def home():
    ip = get('https://api.ipify.org').text
    return ('My public IP address is: {}'.format(ip))



