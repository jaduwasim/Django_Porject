from django.shortcuts import render

# Create your views here.

def Page_Count_Views(request):
    print('Cookies:', request.COOKIES)
    count = request.session.get('count',0)
    count = count + 1
    request.session['count'] = count
    request.session.set_expiry(60)
    print('date exipry:', request.session.get_expiry_date())
    print('age exipry:', request.session.get_expiry_age())
    return render(request, 'testapp/pagecount.html',{'count':count})