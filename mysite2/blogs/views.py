from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from django.core import serializers
from .models import Our_users, User_posts
from .forms import FilterForm


# Create your views here.
def index(request):
    posts_list = User_posts.objects.all()
    if request.GET:
        chosen_one = request.GET['filter_by_user']
        posts_list = User_posts.objects.filter(userId = chosen_one)

    posts_dict = {
                    'posts': posts_list,
                    # 'users': users_list,
                    'user_filter_choice' : FilterForm
                  }

    return render(request, 'blogs/index.html', context = posts_dict)



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
            return "File '{}' not found".format(path)
    if model == '':
        model = str(input("Enter model: ")) #MODEL INPUT


    app_name = model.split(".")[0]
    result = []
    for obj in json_data:

        def recu(model, obj, app):
            # print(obj)
            for dikey, dival in list(obj.items()):

                if dikey == 'id':
                    global main_id
                    main_id = dival

                main_key = model.split(".")[1]

                if isinstance(dival,dict):
                    subdic = obj.pop(dikey)
                    subdic["{}_id".format(main_key)] = main_id
                    # print("IN IF {}".format(dikey))
                    # print(subdic)
                    in_model = "{}.{}".format(app,dikey)
                    # in_model = "{}.{}".format(app,main_key)
                    recu(in_model,subdic,app)
            data = [{
                    "model" : model,
                    "fields" : obj
                    }]
            print(data)
            # for ds in serializers.deserialize("json", json.dumps(data)):
            #     ds.save()
                # print("saved")
        recu(model, obj, app_name)

    return 'DONE'
