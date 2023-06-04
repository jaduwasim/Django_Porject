import imp
from django.urls import path
from testapp import views
urlpatterns = [ 
    path('test/',views.template_view),
    path('wish/', views.wish_view)
]