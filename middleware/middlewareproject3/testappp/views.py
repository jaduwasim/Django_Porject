from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(rquest):
    print(10/0)
    return HttpResponse('<h1>Hello This Response from View Function</h1>')