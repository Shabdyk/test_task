# Generated by Django 3.2.9 on 2021-11-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('suite', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Our_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=200)),
                ('website', models.URLField(default='')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.user_address')),
            ],
        ),
    ]