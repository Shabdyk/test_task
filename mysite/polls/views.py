from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def index(request):
    return HttpResponse("Hello its the polls page")

# def loc_json(json_path = 'polls/ini_db.json'):
#     with open(json_path) as f:
#         data_loc = json.load(f)
#     return data_loc
#
# def web_json(json_url = "http://jsonplaceholder.typicode.com/users"):
#     file = requests.get(json_url)
#     return file.json()

def data_fixture(path = '', model = ''):
    def loc_json(json_path):
        with open(json_path) as f:
            data_loc = json.load(f)
        return data_loc
    def web_json(json_url):
        file = requests.get(json_url)
        return file.json()

    if path == '':
        path = str(input("Enter path: "))

    if "http://" or "https://" in path:
        try:
            json_data = web_json(path)
        except JSONDecodeError:
            return "Invalid link"
    else:
        try:
            json_data = loc_json(path)
        except FileNotFoundError:
            return "File {} not found".format(path)

    if model == '':
        model = str(input("Enter model: "))



    result = []
    for obj in json_data:
        data = [
            {
            "model" : model,
            "fields" : obj
            }
        ]
        try:
            for ds in serializers.deserialize("json", json.dumps(data)):
                ds.save()
                result.append('succcess')
        except serializers.base.DeserializationError:
            return "Seems like json-data and models do not correlate"

    return result
