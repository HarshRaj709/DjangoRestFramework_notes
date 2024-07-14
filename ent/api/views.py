from django.shortcuts import render
from django.http import JsonResponse
import json

def home_api(request,*args, **kwargs):
    body = request.body
    print(body)     #json sting  ---> b'{"query": "from server"}'
    data = json.loads(body)
    print(data)         #{'query': 'from server'}
    print(data['query'])    #from server

    get = request.GET
    print(get)          #<QueryDict: {'abc': ['123']}>  ---params are query parameters {params}
    
    post = request.POST
    print('post',post)      #post <QueryDict: {}>   As we are not send anything as POST

    headers = request.headers
    print(headers)          #{'Content-Length': '24', 'Content-Type': 'application/json', 'Host': '127.0.0.1:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    
    return JsonResponse({'message':'hi first api through django'})