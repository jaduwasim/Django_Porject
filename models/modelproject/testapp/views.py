from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def list_data(request):
    data = Student.objects.all()
    st_data = {'data':data}
    return render(request, 'testapp/result.html', st_data)