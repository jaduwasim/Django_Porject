from django.shortcuts import render, HttpResponseRedirect
from account.forms import SignUpForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, 'account/home.html')

# Sign Up 
def signup_view(request):
    fm = SignUpForm()
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'You are Registered Successfull...')
            fm.save()
            return HttpResponseRedirect('/login/')
    return render(request, 'account/signup.html',{'forms':fm})

# Login
def login_view(request):
    fm = AuthenticationForm()
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Your Logedin Successfully...')
                return HttpResponseRedirect('/profile/')
        else:
            messages.success(request, 'Invalid Credentials...')
            return HttpResponseRedirect('/login/')
    return render(request, 'account/login.html',{'forms':fm})

# Logout
def log_out(request):
    logout(request)
    messages.success(request, 'Logout Now')
    return HttpResponseRedirect('/login/')


# Profile
def profile_view(request):
    if request.user.is_authenticated:
        fm = UserUpdateForm(instance=request.user)
        if request.method == "POST":
            fm = UserUpdateForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Data Updated')
                fm.save()
                return render(request, 'account/profile.html',{'form':fm})
        return render(request, 'account/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

