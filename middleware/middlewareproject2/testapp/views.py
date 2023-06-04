from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Middlware_View(request):
    return HttpResponse('<h1>Custom Response from view Functions</h1>')
