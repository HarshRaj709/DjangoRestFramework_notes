import requests
import json

url = "http://127.0.0.1:8000/"

data = {
    'name':'hanan',
    'roll':120,
    'city':'ranchi'
}

json_data = json.dumps(data)
res = requests.post(url = url,data=json_data)

data = res.json()
if 'msg' in data:
        print(data['msg'])
elif 'roll' in data:
    print(data['roll'])
elif 'name' in data:
      print(data['name'])
else:
      print(data['non_field_errors'])
