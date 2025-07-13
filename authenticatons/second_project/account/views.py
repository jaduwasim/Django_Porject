from django.shortcuts import render, HttpResponseRedirect
from account.forms import SignUPForms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup_view(request):
    fm = SignUPForms()
    if request.method == "POST":
        fm = SignUPForms(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your are registerd')
            fm.save()
            return render(request, 'account/signup.html', {'form':fm})
    return render(request, 'account/signup.html', {'form':fm})

def login_view(request):
    fm = AuthenticationForm()
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            print(f'Username : {uname}')
            upass = fm.cleaned_data['password']
            print(f'password: {upass}')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                messages.success(request, 'You are login')
                return HttpResponseRedirect('/profile/')
    return render(request, 'account/login.html',{'form':fm})

def profile_view(request):
    if request.user.is_authenticated:
        fm = UserChangeForm(isinstance=request.user)
        return render(request, 'account/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')