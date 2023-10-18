from django import forms

class NameForm(forms.Form):
    Name = forms.CharField(label='Enter Name')

class AgeForm(forms.Form):
    age = forms.IntegerField(label='Enter Age')

class GFForm(forms.Form):
    gf = forms.CharField(label='Enter GF Name')