from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def SingUp(request):
    fm = UserCreationForm()
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration is success')
            return render(request, 'enroll/singup.html')
    return render(request, 'enroll/singup.html',{'form':fm})