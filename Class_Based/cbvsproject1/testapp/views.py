from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
class Hello_View(View):
    def get(self, request):
        return HttpResponse('<h1>Hello Class Based Views World</h>')

class Template_CBV(TemplateView):
    template_name = 'testapp/home.html'