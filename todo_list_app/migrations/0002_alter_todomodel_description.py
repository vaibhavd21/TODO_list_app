# Generated by Django 3.2.3 on 2021-06-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
