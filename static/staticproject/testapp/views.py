from django.shortcuts import render

# Create your views here.
def reult_views(request):
    brand = {'b1':'KingFisher','b2':'Foster','b3':'Teacher Choice'}
    return render(request, 'testapp/results.html', brand)