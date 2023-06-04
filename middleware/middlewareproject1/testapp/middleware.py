
class MiddleWareAuthentication(object):
    def __init__(self, get_response):
        print('__init__ Magic Method Exicution........')
        self.get_response = get_response

    
    def __call__(self, request):
        print('pre processing execution......')
        response = self.get_response(request)
        print('post processing Exexutions....')
        return response