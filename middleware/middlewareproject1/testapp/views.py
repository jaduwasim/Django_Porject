from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def middleware_view(request):
    print('This line added by views function')
    return HttpResponse('<h1>Hello MiddleWare</h1>')