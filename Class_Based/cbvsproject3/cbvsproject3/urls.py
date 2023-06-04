"""cbvsproject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp.views import Company_List_View, Company_Detail_View, Company_Create_View, Company_Update_View, Compay_Delete_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Company_List_View.as_view(), name='home'),
    path('<int:pk>/',Company_Detail_View.as_view(), name='detail'),
    path('create/', Company_Create_View.as_view()),
    path('update/<int:pk>/', Company_Update_View.as_view()),
    path('delete/<int:pk>/', Compay_Delete_View.as_view()),
]
