import requests

url = 'http://127.0.0.1:8000/products/'

response = requests.get(url,params={'abc':123},json={'query':'from server'})    #used to send data which is inside params and json

print(response.status_code)
print(response.text)
# print(response.json()['message'])
# print(response.json())