import requests
import json

url = "http://127.0.0.1:8000/api/"

def data_post(name,roll,city):
    data = {
        'name':name,
        'roll':roll,
        'city':city
    }

    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    res = requests.post(url=url,headers=header,data = json_data)

    jsoned = res.json()
    only = jsoned['msg']
    print(only)

# data_post()

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    res = requests.get(url=url, headers=header ,data=json_data)
    jsoned = res.json()
    print(jsoned)

# get_data(1)

def update_data(id,name,roll,city):
    data={
        'id':id,
        'name':name,
        'roll':roll,
        'city':city
    }

    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    res = requests.put(url=url,headers=header,data=json_data)

    string = res.json()
    print(string)

# update_data()

def delete_data(id):
    data = {
        'id':id
    }

    json_data = json.dumps(data)
    header = {'content-Type':'application/json'}
    res = requests.delete(url=url,headers=header,data=json_data)

    data = res.json()
    print(data)

# delete_data(2)

while True:
    print('------------Welcome User i hope you are doing well----------------------')
    print('--------------------This is api based CRUD App--------------------------')
    print('''
            select option 1: To enter data
            select option 2: To retrieve data
            select option 3: To update data
            select option 4: To delete data
            select option 5: To Exit

            ''')

    user_input = int(input('Enter your choice .. '))

    if user_input==1:
        name = input('Enter Student name = ')
        roll = int(input('Enter Student roll no. = '))
        city = input('Enter Student city = ')
        data_post(name,roll,city)
    elif user_input==2:
            get_data()
    elif user_input==3:
        id = input('enter id no. you want to update = ')
        name = input('enter name you want to update = ')
        roll = input('enter roll no. you want to update = ')
        city = input('enter city you want to update = ')
        update_data(id,name,roll,city)
    elif user_input==4:
        id  =  int(input('Enter id of Entry to delete'))
        delete_data(id)
    else:
        print('Exit successfully')
        break