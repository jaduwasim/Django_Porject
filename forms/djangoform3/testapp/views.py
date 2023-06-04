from django.shortcuts import render
from . import forms
# Create your views here.
def StudentInputView(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing Information:')
            print('-------------------------------------------------')
            print(form.cleaned_data)
            print('Name:        ',form.cleaned_data['name'])
            print('Roll Number: ',form.cleaned_data['rollno'])
            print('Email:       ',form.cleaned_data['email'])
            print('Feedback:    ',form.cleaned_data['feedback'])

    return render(request, 'testapp/feedback.html',{'form':form})