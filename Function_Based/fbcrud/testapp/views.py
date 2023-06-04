from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.models import EmployeeModel
from testapp.forms import EmployeeForm

# Create your views here.
def index(request):
    emp_data = EmployeeModel.objects.all()
    return render(request, 'testapp/index.html',{'empdata':emp_data})

def Insert_View(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.is_valid()
        form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'testapp/form.html',{'form': form})

def Delete_View(request, id):
    data = EmployeeModel.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/home')

def Update_View(request, id):
    data = EmployeeModel.objects.get(id=id)
    form = EmployeeForm(instance=data) # instance for update the is fulfiill because of it!!!!
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data) #if you will not take instance, then new record will create!
        form.is_valid()
        form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'testapp/form.html',{'form':form})
    
