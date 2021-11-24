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

    def recu(json_data,model):
        app_name = model.split(".")[0]
        result = []
        for obj in json_data:

            def recu(model, obj, app):
                for dikey, dival in list(obj.items()):
                    if isinstance(dival,dict):
                        subdic = obj.pop(dikey)
                        # print(dikey, subdic)
                        model = "{}.{}".format(app,dikey)
                        recu(model,subdic,app)
                data = [{
                        "model" : model,
                        "fields" : obj
                        }]
                print(data)

            recu(model, obj, app_name)



            # def recur(obj,model):
            #     rec_data = []
            #     for obkey, obval in zip(obj,obj.values()):
            #         # print(obkey, obval)
            #         if isinstance(obval, dict):
            #             # print('rec', obkey, obval)
            #
            #             data = [
            #                 {
            #                 "model" : obkey,
            #                 "fields" : obval,
            #                 }
            #             ]
            #             recur(obval,obkey)
            #             rec_data.append(data)
            #     return rec_data
            # result.append(recur(obj,model))


            # result.append(data)
        return result

    return recu(json_data,model)

        # for ds in serializers.deserialize("json", json.dumps(data)):
            # ds.save()

            # print(ds.object)



    # return data
