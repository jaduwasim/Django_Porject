from django.shortcuts import render
from . import forms
# Create your views here.
def StudentViews(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid:
            form.save()
    return render(request, 'testapp/studentform.html', {'form':form})
