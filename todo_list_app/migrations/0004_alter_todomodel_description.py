# Generated by Django 3.2.3 on 2021-06-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0003_alter_todomodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
