from django.shortcuts import render
from testapp import forms
# Create your views here.

def Student_View(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'testapp/form.html', {'form':form})
# def Add_Movie_View(request):
#     form = forms.MoviesForm()
#     if request.method == 'POST':
#         form = forms.MoviesForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'testapp/addmovie.html',{'form':form})
