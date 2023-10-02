from requests import get


def home():
    ip = get('https://api.ipify.org').text
    return data = print('My public IP address is: {}'.format(ip))

