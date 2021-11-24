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
            return "File '{}' not found".format(path)                 #CHECK IF PATH IS LOCAL
    if model == '':
        model = str(input("Enter model: ")) #MODEL INPUT

    def recu(json_data,model):
        # appname = model.split(".")[0]
        result = []
        for obj in json_data:
            # print('obj ', obj)
            def recur(obj,model):
                for obkey, obval in zip(obj,obj.values()):
                    # print(obkey, obval)
                    if isinstance(obval, dict):
                        # print('rec', obkey, obval)
                        recur(obval,obkey)
                        data = [
                            {
                            "model" : model,
                            "fields" : obval,
                            }
                        ]

                return data
            return recur(obj,model)


            # result.append(data)
        return result

    return recu(json_data,model)

        # for ds in serializers.deserialize("json", json.dumps(data)):
            # ds.save()

            # print(ds.object)



    # return data
