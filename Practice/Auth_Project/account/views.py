from django.shortcuts import render
from account.forms import StudentSingUpForm

# Create your views here.

def SignUpView(request):
    fm = StudentSingUpForm()
    if request.method == 'POST':
        fm = StudentSingUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request, 'account/signup.html', {'forms':fm})