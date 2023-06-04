from django.shortcuts import render
import datetime
import random

# Create your views here.
def result_view(request):
    msg_list = [
        'The Golden days Ahead',
        'Tomorrow is the perfect day to propose your Girl Friend',
        'Better to Sleep time even in office',
        'Tomorrow will be the best day of Your Life',
        'very soon you will get Job'
    ]
    names_list = ['Sunny Leone','Malika Sherawat','Katrina Kaif','Kareena Kapoor','Priyanka Chopra']
    time =  datetime.datetime.now()
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Good Morning'
    elif h<16:
        s = 'Good Afternoon'
    elif h<18:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'name':name,'msg':msg, 'wish':s}
    return render(request, 'testapp/astrology.html', my_dict)