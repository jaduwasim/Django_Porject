from django.shortcuts import render
from .models import City, Country
# Create your views here.
def home(request):
    data = Country.objects.values('id','name','city__name','city__population', 'city__id').order_by('city__id')
    return render(request, 'testapp/home.html', {'data':data})