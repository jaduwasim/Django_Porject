from django import forms
from account.models import UserModel
from django.contrib.auth.forms import UserCreationForm

class SignUPForms(UserCreationForm):
    class Meta:
        model = UserModel
        fields =['email','phone','first_name','last_name']
