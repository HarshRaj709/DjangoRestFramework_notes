from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from .models import Products
from django.forms.models import model_to_dict

# Create your views here.
def home_api(request,*args, **kwargs):
    model_data = Products.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data,fields=('id','title'))
    # return JsonResponse(data)
    return HttpResponse(data)