from requests import get

class handler():
    def home():
        ip = get('https://api.ipify.org').text
        data = print('My public IP address is: {}'.format(ip))
        return data
    
