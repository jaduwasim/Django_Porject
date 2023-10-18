from django.shortcuts import render
from testapp.forms import ItemForms
# Create your views here.

def item(request):
    request.session.set_expiry(0)
    form = ItemForms()
    if request.method == 'POST':
        name = request.POST['name']
        quan = request.POST['quan']
        request.session[name] = quan

    return render(request, 'testapp/item.html', {'forms':form})

def result(request):
    return render(request, 'testapp/result.html')