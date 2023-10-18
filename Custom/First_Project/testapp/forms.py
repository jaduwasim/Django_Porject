from django import forms
from testapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email', 'name', 'password', 
        ]