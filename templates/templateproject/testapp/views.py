from django.shortcuts import render
import datetime

# Create your views here.
def template_view(request):
    dt=datetime.datetime.now()
    name ='washim'
    roll=100
    marks = 100
    my_dict={'date':dt,'name':name,'roll':roll,'marks':marks}
    return render(request,'testapp/results.html', my_dict)

def wish_view(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest!!! Very Very Good'
    h=int(date.strftime('%H'))
    if h<12:
        msg+='Morning!!!'
    elif h<16:
        msg+='AfterNoon!!!'
    elif h<21:
        msg+='Evening!!!'
    else:
        msg='Hello Guest!!! Very Very Good Night'
    my_dict = {'date':date, 'insert_meg':msg}
    return render(request, 'testapp/wish.html', my_dict)