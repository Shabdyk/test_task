# Generated by Django 3.2.9 on 2021-11-23 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20211123_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_geo',
            name='our_user_address',
        ),
        migrations.RemoveField(
            model_name='our_users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='our_users',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='our_users',
            name='website',
        ),
        migrations.DeleteModel(
            name='User_address',
        ),
        migrations.DeleteModel(
            name='User_geo',
        ),
    ]
