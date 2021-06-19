from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import User
# Create your models here.
class TODOModel(models.Model):
    status_choice = [
        ('C','Completed'),
        ('P','Pending')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=200,null=True,blank=True)
    status = models.CharField(max_length=2,choices=status_choice)
    created = models.DateTimeField(auto_now_add=True)