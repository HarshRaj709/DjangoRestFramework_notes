import requests
import json

URL = 'http://127.0.0.1:8000/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}            #this is python dict, so we have to convert it to json type.
    json_data = json.dumps(data)        #converted python dictionary to json data.
    r= requests.get(url = URL,data = json_data)     #here we used GET method
    data = r.json()
    print(data)
    

# get_data()
    

def post_data():
    data = {
        'name':'kohinoor',
        'roll':106,
        'city':'bareli',
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)       #there may be a chances that we get some notification or data after saving user we will show it thorugh r
    data = r.json()       #here we converted our data back to json to show it in frontend.
    print(data)

# post_data()
    

def update_data():
    data = {
        'id':4,
        'name':'new',
        # 'roll':106,
        'city':'bareli',
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL,data = json_data)       #there may be a chances that we get some notification or data after saving user we will show it thorugh r
    data = r.json()       #here we converted our data back to json to show it in frontend.
    print(data)

# update_data()
    
def delete_data():
    data = {'id':6}

    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)   # here we write delete
    data = r.json()       #here we converted our data back to json to show it in frontend.
    print(data)

delete_data()
