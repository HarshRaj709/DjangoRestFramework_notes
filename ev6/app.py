import requests
import json

url = "http://127.0.0.1:8000/student_create/"

def create_data():
    data = {
        'name':'Varah',
        'roll':103,
        'city':'kolkate'
    }

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.post(url=url,headers = headers,data=json_data)

    data = res.json()
    print(data)
create_data()

def update_data(id):
    data = {
        'id':id,
        'name':'Pankaj Maurya',
        'roll':112,
        'city':'barabanki'
    }

    json_data = json.dumps(data)
    res = requests.put(url=url,data=json_data)

    data = res.json()
    print(data)

# update_data(2)