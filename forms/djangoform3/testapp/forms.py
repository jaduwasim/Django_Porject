import imp
from socket import fromshare
from unicodedata import name
from wsgiref.validate import validator
from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    # Django's Inbuilt Core Validators:
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(40)])


    # Explicitly by the Programmer by using Clean Methods:
    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('The Mainimum No. of characters in the Name Fields should be 4')
        return inputname

    