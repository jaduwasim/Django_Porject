from unicodedata import name
from django import forms

class StudentForm(forms.Form):
    Name=forms.CharField(max_length=64)
    Marks=forms.IntegerField()