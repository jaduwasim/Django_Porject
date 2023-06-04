from django.shortcuts import render
from testapp import forms
from testapp.models import Movie

# Create your views here.

def Index_View(request):
    return render(request, 'testapp/index.html')

def Add_Movie_View(request):
    form = forms.MoviesForm()
    if request.method == 'POST':
        form = forms.MoviesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/addmovie.html',{'form':form})

def List_Movie_View(request):
    movies = Movie.objects.all()
    return render(request, 'testapp/listmovies.html',{'movies':movies})
