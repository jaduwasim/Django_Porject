from django.http import HttpResponse
class AppMaintenceMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        return HttpResponse('<h1>Currently Applicaton under Maintenance... please try after 2 days !!!</h>')