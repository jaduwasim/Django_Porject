from pickletools import read_unicodestring1
from django.shortcuts import render
from . import forms
# Create your views here.

def studentinputview(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request, 'testapp/input.html', my_dict)
'''
Alternative Way:
def studentinputview(request):
    form=forms.StudentForm()
    return render(request, 'testapp/input.html', {'form':form})
'''