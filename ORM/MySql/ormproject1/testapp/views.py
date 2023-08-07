from django.shortcuts import render
from testapp.forms import EmployeeForm
from testapp.models import Employee
from django.db.models import Avg, Max, Min, Sum, Count
# Create your views here.

def Employee_View(request):
    emp = EmployeeForm()
    if request.method == 'POST':
        emp = EmployeeForm(request.POST)
        if emp.is_valid():
            emp.save()
        return index_view(request) 
    return render(request, 'testapp/home.html', {'emp':emp})

def index_view(request):
    # emp_data = Employee.objects.all()
    # emp_data = Employee.objects.filter(esal__gte = 15000)
    # emp_data = Employee.objects.filter(esal__lte = 15000)
    # emp_data = Employee.objects.filter(ename__exact ='Washim') #(Here case is not applicable but we can user iexact and exact)
    # emp_data = Employee.objects.filter(ename__icontains = 'w') # (Here is case is applicable when we use contains , case will not applicable when we use icontains)
    # emp_data = Employee.objects.filter(id__in = [1,2,3]) # in Mehtod
    # emp_data = Employee.objects.filter(ename__startswith = 'wa')
    # emp_data = Employee.objects.filter(ename__endswith='s')
    emp_data = Employee.objects.filter(esal__range = [10000,15000])
    # emp_data = Employee.objects.get(id=1)
    return render(request, 'testapp/index.html', {'emp_list':emp_data})

def index_view2(request):
    emp = Employee.objects.filter(ename__startswith='D').only('ename','esal').order_by('ename')
    return render(request, 'testapp/test.html', {'emp_list':emp})

def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    aggregate = {'avg':avg['esal__avg'],'min':min['esal__min'],'max':max['esal__max'],'sum':sum['esal__sum'], 'count':count['esal__count']}
    return render(request, 'testapp/aggregate.html', aggregate)