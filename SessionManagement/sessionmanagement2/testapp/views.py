from urllib import response
from django.shortcuts import render

# Create your views here.
'''Session Management by using Cookies
 (PageCount Application)'''

def count_view(request):
    print('Request:',request)
    if 'count' in request.COOKIES:
        print('Request.COOKIES:',request.COOKIES)
        newcount=int(request.COOKIES['count'])+1
        print('NewCount:',newcount)
    else:
        newcount=1
    response=render(request, 'testapp/count.html',{'count':newcount})
    print('Respone:',response)
    response.set_cookie('count',newcount)
    return response