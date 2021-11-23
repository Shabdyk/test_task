import requests
from django.core import serializers

def access_json(json_url = "http://jsonplaceholder.typicode.com/users"):

    result = []
    file = requests.get(json_url)
    data = file.json()

    # for obj in data:
    #     result.append(obj)



    for obj in serializers.deserialize("json", str(data)):
        result.append("suc")

    return result

print(access_json())
