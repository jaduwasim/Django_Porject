from django.http import HttpResponse
class ErroExceptionMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        # return HttpResponse('<h1>Currently we are facing some technical problem!!!</h1>')
        return HttpResponse(f'<h1>Currently we are facing some techical problem <br>The Raised Exception : {exception.__class__.__name__}<br>The Exception Message: {exception}</h1>')
