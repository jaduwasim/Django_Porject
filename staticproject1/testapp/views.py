from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg=None
    h=int(date.strftime('%H'))
    if h<12:
        msg='Hello Guest !!!! Very Very Good Morning!!!'
    elif h<16:
        msg='Hello Guest !!!! Very Very Good AfterNoon!!!'
    elif h<21:
        msg='Hello Guest !!!! Very Very Good Evening!!!'
    else:
        msg='Hello Guest !!!! Very Very Good Night!!!'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'testApp/wish.html',context=my_dict) 