from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# class User_address(models.Model):
#     street = models.CharField(max_length = 200)
#     suite = models.CharField(max_length = 200)
#     city = models.CharField(max_length = 200)
#     zipcode = models.CharField(max_length = 200)
    # address = models.ForeignKey(Our_users, on_delete = models.CASCADE)

class Our_users(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50, default = "")
    phone = models.CharField(max_length = 200, default = "")
    website = models.URLField(max_length = 200, default = "")
    # address = models.ForeignKey(User_address, on_delete = models.CASCADE)
    address = models.JSONField(null = True) #NOT RIGHT
    company = models.JSONField(null = True) #NOT RIGHT

    def __str__(self):
        return self.username
#


#
# class User_geo(models.Model):
#     lat = models.CharField(max_length=128)
#     lng = models.CharField(max_length=128)
#     our_user_address = models.ForeignKey(User_address, on_delete = models.CASCADE)



# class Question(models.Model):
#     question_text = models.CharField(max_length = 200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete = models.CASCADE)
#     choice_text = models.CharField(max_length = 200)
#     votes = models.IntegerField(default = 0)
#
#     def __str__(self):
#         return self.choice_text
