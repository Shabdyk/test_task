# Generated by Django 3.2.9 on 2021-11-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20211123_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_users',
            name='address',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='User_address',
        ),
    ]
