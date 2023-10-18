# def CustomMiddlewar(get_response):
#     print('This code execution at the time of running server')
#     def My_Middleware(request):
#         print('This code execute befor the request processing')
#         response = get_response(request)
#         print('This code Execut after request processing')
#         return response
#     return My_Middleware

class CustomMiddlewar(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('This code execution at the time of running server')
    
    def __call__(self, request):
        print('This code execute befor the request processing')
        response = self.get_response(request)
        print('This code Execut after request processing')
        return response
    
    def process_exception(self, request, exception):
        print('we are phasing some technical issues!!!')