from dataclasses import field, fields
from django.forms import ModelForm
from todolist.models import Task

class InputForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description'
        ]