from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from testapp.models import Beer
from django.urls import reverse_lazy

# Create your views here.

def Home_Views(request):
    return render(request, 'testapp/home.html')

class BeerListView(ListView):
    model = Beer
    # Default Template File : beer_list.html
    # Default Context Object Name = beer_list

class BeerDetailView(DetailView):
    model = Beer
    # default Template file = beer_detail.html
    # default context object name = beer or object

class BeerCreateView(CreateView):
    model = Beer
    fields = '__all__'
    # default template file = beer_form.html

class BeerUpdateView(UpdateView):
    model = Beer
    fields = ['taste',]
    # default template file = beer_form.html

class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('home')
    # default template file = beer_confirm_delete.html
