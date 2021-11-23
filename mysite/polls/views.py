from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello its the polls page")


import requests
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder



def access_json(json_url = "http://jsonplaceholder.typicode.com/users"):

    result = []
    file = requests.get(json_url)
    data_json = file.json()

    return data_json
