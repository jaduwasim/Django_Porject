from django import forms

class StudentFrom(forms.Form):
    Name = forms.CharField(max_length=30)