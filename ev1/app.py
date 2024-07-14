import requests
url  = 'http://127.0.0.1:8000/'


response = requests.get(url)
data = response.json()      # to call only json data
print(data)