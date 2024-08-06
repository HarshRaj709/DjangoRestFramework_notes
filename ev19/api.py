import requests
import json

url = "http://127.0.0.1:8000/StudentApi/"

def post():
    data = {
        "name": "harsh",
        "roll": 101,
        "city": "lucknow"
    }

    send = json.dumps(data)
    header = {'content-Type':'application/json'}
    res = requests.post(url=url,headers=header,data=send)
    data = res.json()
    print(data)

post()