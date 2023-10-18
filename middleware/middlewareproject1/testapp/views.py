from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def middleware_view(request):
    print('This line added by views function')
    return HttpResponse('<h1>Hello MiddleWare</h1>')

def page_count(request):
    count = int(request.COOKIES.get('count',0))
    count = count+1
    response = render(request, 'testapp/count_page.html', {'count':count})
    response.set_cookie('count',count)
    return response 