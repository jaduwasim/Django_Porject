from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from enroll.forms import SignUpForm

# Create your views here.

def SignUpView(request):
    fm = SignUpForm()
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration Success!!!')
            return render(request, 'enroll/signup.html')
    return render(request, 'enroll/signup.html',{'form':fm})
