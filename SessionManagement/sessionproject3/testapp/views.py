from django.shortcuts import render
from testapp import forms
import datetime

# Create your views here.

def Student_Views(request):
    form = forms.StudentFrom()
    return render(request, 'testapp/home.html',{'form':form})

def Date_Time_Views(request):
    name=request.GET['Name'] 
    response = render(request, 'testapp/datetime.html', {'name':name})
    response.set_cookie('Name',name)
    return response

def Result_Views(request):
    name = request.COOKIES['Name']
    date_time = datetime.datetime.now()
    response = render(request, 'testapp/result.html', {'name':name,'date_time':date_time})
    return response