import requests

URL = 'http://127.0.0.1:8000/stu_all/'

r = requests.get(url = URL)

data = r.json()
print(data,end='')