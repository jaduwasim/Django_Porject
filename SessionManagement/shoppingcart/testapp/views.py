from django.shortcuts import render
from testapp.forms import ItemAddForm


# Create your views here.

def Index(request):
    return render(request, 'testapp/home.html')

def Add_Item_Views(request):
    form = ItemAddForm()
    response = render(request, 'testapp/additem.html',{'form':form})
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity, 180)
    return response

def Display_Item(request):
    return render(request, 'testapp/display.html')