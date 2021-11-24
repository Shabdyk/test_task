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
    def __str__(self):
        return self.name

class Address(models.Model):
    our_user =  models.ForeignKey("Our_users", on_delete = models.CASCADE)
    street = models.CharField(max_length = 200)
    suite = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 200)

class Company(models.Model):
    our_user =  models.ForeignKey("Our_users", on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    catchPhrase = models.CharField(max_length = 200)
    bs = models.CharField(max_length = 200)

class Geo(models.Model):
    address = models.ForeignKey("Address", on_delete = models.CASCADE)
    lat = models.CharField(max_length = 50)
    lng = models.CharField(max_length = 50)

class User_posts(models.Model):
    userId = models.ForeignKey("Our_users", on_delete = models.CASCADE, to_field = 'id')
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
        return self.title
