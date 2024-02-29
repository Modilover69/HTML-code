import requests

url = 'https://play.vishwactf.com/login'

data = {
    'username':'Darry',
    'current-password':'Hyper@69'
}
r = requests.post(url=url,data=data)

print(r.text)