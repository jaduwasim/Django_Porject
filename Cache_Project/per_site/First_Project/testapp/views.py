from django.shortcuts import render

# Create your views here.
def coures(request):
    return render(request, 'testapp/course.html')