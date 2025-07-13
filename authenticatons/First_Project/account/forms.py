from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UserUpdateForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

        