from django import forms

from .models import Student


class MyForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", ]
        labels = {'first_name': "Name", "last_name": "Surname", "age": 0, }
