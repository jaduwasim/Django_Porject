from django.shortcuts import render
from .models import Post
# Create your views here.
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'testapp/home.html',{'posts':posts})