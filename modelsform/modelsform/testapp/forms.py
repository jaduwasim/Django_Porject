from django import forms
from testapp.models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
