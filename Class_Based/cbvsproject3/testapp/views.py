from django.shortcuts import render
from django.views.generic import ListView, DetailView ,CreateView, UpdateView, DeleteView
from testapp.models import Company
from django.urls import reverse_lazy

# Create your views here.

class Company_List_View(ListView):
    # Default Templates File Name = company_list.html
    # Default Context Object Name = company_list
    model = Company

class Company_Detail_View(DetailView):
    # Dafault Templates File Name = company_detail.html
    # default context object name = company or object
    model = Company

class Company_Create_View(CreateView):
    # Default templates file name = company_form.html
    model = Company
    fields = '__all__'

class Company_Update_View(UpdateView):
    # Default templates name = company_form.html
    model = Company
    fields = '__all__'

class Compay_Delete_View(DeleteView):
    # Default templates name = company_confirm_delete.html
    model = Company
    success_url = reverse_lazy('home')