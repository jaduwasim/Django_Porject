from django.urls import path
from testapp import views
urlpatterns = [
    path('registration/', views.UserRegistration.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]