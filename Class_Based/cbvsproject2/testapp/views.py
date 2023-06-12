from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView , UpdateView, DeleteView
from testapp.models import Book
from django.urls import reverse_lazy

# Create your views here.


class Book_List_View(ListView):
    # Default Template file name = book_list.hmtl
    # Defailt Context Object Name = book_list
    # we can create our own template file name:
    # template_name = 'template_file_location/file_name.html'
    model = Book

class Book_Detail_View(DetailView):
    # Default Template file name = book_detail.hmtl
    # Defailt Context Object Name = book or object
    model = Book

class Book_Create_View(CreateView):
    # Default Template file name = book_form.hmtl
    model = Book
    fields ='__all__'

class Book_Update_View(UpdateView):
    # Default Template file name = book_form.hmtl
    model = Book
    fields ='__all__'

class Book_Delete_View(DeleteView):
    # Default Template file name = book_confirm_delete.html
    model = Book
    success_url = reverse_lazy('home')