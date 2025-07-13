from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from student.models import StudentUser

class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(label="Date of Birth",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    class Meta:
        model = StudentUser
        fields = ['username','first_name','last_name','email','image','date_of_birth','phone','class_name']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email Address','phone':'Mobile No.','image':'Profile Picture','class_name':'Class'}

class ProfileEditForm(UserChangeForm):
    password =None
    date_of_birth = forms.DateField(label="Date of Birth",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"])
    class Meta:
        model = StudentUser
        fields = ['first_name','last_name','email','image','date_of_birth','phone','class_name']