# Generated by Django 3.2.9 on 2021-11-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20211123_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_users',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='our_users',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='our_users',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
