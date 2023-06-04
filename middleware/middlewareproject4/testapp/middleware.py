
class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print('This line printed by First Middleware at pre-processing of requesst')
        response = self.get_response(request)
        print('This line printed by first Middleware at post-processing of request')
        return response

class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print('This line printed by second middleware at pre-processing of request')
        response = self.get_response(request)
        print('This line printed by second middleware at post-processing of request')
        return response