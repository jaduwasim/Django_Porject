from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, GFForm
# Create your views here.

def home(request):
    form = NameForm()
    return render(request, 'testapp/home.html', {'forms':form})

def age(request):
    name = request.GET['Name']
    request.session['Name'] = name
    form = AgeForm()
    return render(request, 'testapp/age.html', {'forms':form, 'name':name})

def gf(request):
    name = request.session['Name']
    age = request.GET['age']
    request.session['age'] = age
    form = GFForm()
    return render(request, 'testapp/gf.html',{'forms':form, 'name':name})

def result(request):
    name = request.session['Name']
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'testapp/result.html', {'name':name})
