from django import forms

class ItemForms(forms.Form):
    name = forms.CharField(label='Enter Item Name')
    quan = forms.IntegerField(label='Quantity')