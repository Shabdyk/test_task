from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def index(request):
    return HttpResponse("Hello its the polls page")

def loc_json(json_path = 'polls/ini_db.json'):
    with open(json_path) as f:
        # json.dump(doubleQString ,f)
        data_loc = json.load(f)

    return data_loc

def web_json(json_url = "http://jsonplaceholder.typicode.com/users"):

    result = []
    file = requests.get(json_url)
    data_json = file.json()
    return data_json

def data_fixture(json_data):
    result = []
    for obj in json_data:
        ke = 1
        data = [
            {
            "pk" : ke,
            "model" : "polls.our_users",
            "fields" : obj
            }
        ]
        ke =+ 1

        for ds in serializers.deserialize("json", json.dumps(data)):
            ds.save()
            result.append('suc')

    return result
