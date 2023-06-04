from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, GfForm

# Create your views here.

def Name_View(request):
    form = NameForm()
    return render(request, 'testapp/name.html',{'form':form})

def Age_View(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request,'testapp/age.html', {'form':form, 'name':name})

def Gf_View(request):
    age = request.GET['age']
    request.session['age'] = age
    name = request.session['name']
    form = GfForm()
    return render(request, 'testapp/gf.html',{'form':form, 'name':name})

def Result_View(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'testapp/result.html')
