from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from django.core import serializers
from .models import Our_users, User_posts
from .forms import FilterForm


# Create your views here.
def index(request):

    users_list = Our_users.objects.all()
    posts_list = User_posts.objects.all()
    filter_form = FilterForm

    posts_dict = {
                    'posts': posts_list,
                    'users': users_list,
                    'user_filter_choice' : filter_form
                  }

    return render(request, 'polls/index.html', context = posts_dict)

def loc_json(json_path):
    with open(json_path) as f:
        data_loc = json.load(f)
    return data_loc
def web_json(json_url):
    file = requests.get(json_url)
    return file.json()

def data_fixture(path = '', model = ''):

    if path == '':
        path = str(input("Enter path: ")) #FILE-PATH INPUT
    if "http://" in path:
        try:
            json_data = web_json(path)
        except:
            return "Invalid link"
 #CHECK IF PATH IS WEB-URL
    else:
        try:
            json_data = loc_json(path)
        except FileNotFoundError:
            return "File '{}' not found".format(path)                 #CHECK IF PATH IS LOCAL
    if model == '':
        model = str(input("Enter model: ")) #MODEL INPUT

    result = []
    for obj in json_data:
        data = [
            {
            "model" : model,
            "fields" : obj
            }
        ]
        try: #AT THE END TRY RECCURSION
            for ds in serializers.deserialize("json", json.dumps(data)):
                try:
                    ds.save()
                    result.append('suc')
                    # print(ds.object.address)
                except:
                    if len(result) == 0:
                        return "Database was not updated due to the database error"
                    else:
                        return "Some data stored, but proccess interrupted by database error"

        except serializers.base.DeserializationError:
            return "Seems like json-data and models do not correlate"

    return "Database updated. Model: " + model
