from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Our_users(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50, default = "")
    phone = models.CharField(max_length = 200, default = "")
    website = models.URLField(max_length = 200, default = "")
    address = models.ForeignKey("User_address", on_delete = models.CASCADE)
    company = models.ForeignKey("User_company", on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class User_address(models.Model):
    street = models.CharField(max_length = 200)
    suite = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 200)
    geo = models.ForeignKey("User_geo", on_delete = models.CASCADE)

class User_company(models.Model):
    name = models.CharField(max_length = 100)
    catchPhrase = models.CharField(max_length = 200)
    bs = models.CharField(max_length = 200)

class User_geo(models.Model):
    lat = models.CharField(max_length = 50)
    lng = models.CharField(max_length = 50)

class User_posts(models.Model):
    userId = models.ForeignKey("Our_users", on_delete = models.CASCADE, to_field = 'id')
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
        return self.title
