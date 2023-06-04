from django.urls import path
from testapp.views import BeerListView, BeerDetailView, BeerCreateView, BeerUpdateView, BeerDeleteView

urlpatterns =[
    path('', BeerListView.as_view(),name='home'),
    path('<int:pk>/', BeerDetailView.as_view(), name='update'),
    path('create/', BeerCreateView.as_view()),
    path('update/<int:pk>/',BeerUpdateView.as_view()),
    path('delete/<int:pk>/',BeerDeleteView.as_view()),
]