from django.shortcuts import render

# Create your views here.
def count(request):
    count = request.session.get('count',0)
    count = count + 1
    request.session['count'] = count
    print('Session Time:',request.session.get_expiry_age())
    print('Session Time:',request.session.get_expiry_date())
    return render(request, 'testapp/count.html', {'count':count})