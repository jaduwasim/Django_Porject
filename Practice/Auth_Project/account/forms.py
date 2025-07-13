from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import StudentUser

class StudentSingUpForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ('username','first_name', 'last_name', 'image', 'phone', 'is_active','is_staff')
        labels = {
            'username':'Username',
            'first_name' : 'First Name',
            'is_active':'Active'
        }