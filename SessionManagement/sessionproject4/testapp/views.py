from django.shortcuts import render

# Create your views here.
def Home_Views(request):
    return render(request, 'testapp/home.html')

def Age_Views(request):
    print(request.COOKIES)
    username = request.GET['name']
    response = render(request, 'testapp/age.html',{'name':username})
    response.set_cookie('name',username)
    return response

def gf_Views(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.GET['age']
    response = render(request, 'testapp/gf.html', {'name':username})
    response.set_cookie('age',age)
    return response

def Result_Views(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    response = render(request, 'testapp/result.html',{'name':username, 'age':age, 'gf':gf})
    response.set_cookie(gf, max_age=60)
    return response