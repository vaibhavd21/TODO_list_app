from todo_list_app.models import TODOModel
from django.forms import ModelForm, fields, models
from .models import TODOModel


class TODOForm(ModelForm):
    class Meta:
        model = TODOModel
        fields = ['title','description','status']