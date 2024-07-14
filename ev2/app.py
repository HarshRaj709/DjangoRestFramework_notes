import requests
import json

url = "http://127.0.0.1:8000/send/"

# data = requests.get(url=url)

# converted = data.json()
# print(converted)

data = {
    'name':'Ashish Bajpai',
    'roll':102,
    'city':'Kanpur'
}

json_data = json.dumps(data)
response = requests.post(url,json_data)     #response will catch response from request post

datas = response.json()
msg = datas['msg']
print(msg)