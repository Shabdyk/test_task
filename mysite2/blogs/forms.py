from django import forms
from .models import Our_users

all_users = Our_users.objects.all()

ALL_USERS = []
# for i, usr in enumerate(all_users):
#     ALL_USERS.append(('{}'.format(i), usr.name))
# ALL_USERS = tuple(ALL_USERS)

for usr in all_users:
    ALL_USERS.append((str(usr.id), usr.name))
ALL_USERS = tuple(ALL_USERS)

class FilterForm(forms.Form):
    filter_by_user = forms.ChoiceField(choices = ALL_USERS, label = '')
