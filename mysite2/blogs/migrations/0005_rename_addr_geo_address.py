# Generated by Django 3.2.9 on 2021-11-24 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20211124_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geo',
            old_name='addr',
            new_name='address',
        ),
    ]