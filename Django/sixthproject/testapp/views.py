from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
	return HttpResponse('<h1>Response from First View</h1>')

def second_view(request):
	return HttpResponse('<h1>Response from Second View</h1>')

def third_view(request):
	return HttpResponse('<h1>Response from Third View</h1>')

def fourth_view(request):
	return HttpResponse('<h1>Response from Fourth View</h1>')
	
def fifth_view(request):
	return HttpResponse('<h1>Response from Fifth View</h1>')