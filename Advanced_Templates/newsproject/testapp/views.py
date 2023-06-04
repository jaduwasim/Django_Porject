from django.shortcuts import render

# Create your views here.
def Home_Views(request):
    return render(request, 'testapp/home.html')

def Movies_Views(request):
    return render(request, 'testapp/movies.html')

def Sports_Views(request):
    return render(request, 'testapp/sports.html')

def Politics_Views(request):
    return render(request, 'testapp/politics.html')