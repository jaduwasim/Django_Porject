from django.shortcuts import render
from testapp.models import Employees,Jobs,Books

# Create your views here.

def Employees_Data(request):
    print('Request:',request)
    emp_list=Employees.objects.all() 
    print('Emp_List:',emp_list)
    my_dict={'emp_list':emp_list}
    return render (request,'testapp/emp.html', my_dict)

def Jobs_Data(request):
    Jobs_List=Jobs.objects.all()
    my_dict={'jobs_list':Jobs_List}
    return render(request,'testapp/jobs.html',my_dict)

def Books_Data(request):
    book_list=Books.objects.all()
    my_dict={'book_list':book_list}
    return render(request,'testapp/books.html',my_dict)