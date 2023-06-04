from pickletools import read_unicodestring1
from django.shortcuts import render
from . import forms
# Create your views here.

def studentinputview(request):
    sent=False
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print('Form Validating Success And Printing Data:')
            print('--------------------------------------------')
            print('Name:',form.cleaned_data['Name'])
            print('Marks:',form.cleaned_data['Marks'])
            sent = True
    # my_dict = {'form': form}
    return render(request, 'testapp/input.html',{'form': form, 'sent':sent})
'''
Alternative Way:
def studentinputview(request):
    form=forms.StudentForm()
    return render(request, 'testapp/input.html', {'form':form})
'''