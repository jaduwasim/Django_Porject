from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def Home_Page_View(request):
    return render(request, 'testapp/home.html')

@login_required
def Java_Page_View(request):
    return render(request, 'testapp/java.html')

@login_required
def Python_Page_view(request):
    return render(request, 'testapp/python.html')

@login_required
def Apptitude_Page_View(request):
    return render(request, 'testapp/apptitude.html')

def Logout_Page_View(request):
    return render(request, 'testapp/logout.html')

def SingUp_View(request):
    singup = SignUpForm()
    if request.method == 'POST':
        singup = SignUpForm(request.POST)
        user = singup.save()
        user.set_password(user.password) 
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/singup.html',{'form':singup})