# Validation of Total Form directly by using a Single Clean Method


import email
from signal import raise_signal
from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('Total Form Validation')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('Name parameter should start with d')
        inputrollno=total_cleaned_data['rollno']
        if inputrollno<=0:
            raise forms.ValidationError('Roll Should be Greater tha zero')

class SignupForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Recent Password',widget=forms.PasswordInput)
    email=forms.EmailField()

    def clean(self):
        total_clean_data=super.clean()
        pwd=total_clean_data['passsword']
        rpwd=total_clean_data['rpassword']
        if pwd!=rpwd:
            raise forms.ValidationError('Both Password Must be Same!')