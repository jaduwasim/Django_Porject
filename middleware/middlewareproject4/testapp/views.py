from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.
def Home_page_View(request):
    print('This line printed by function views')
    return HttpResponse('<h1>Hello, This Response is from views functions</h1>')