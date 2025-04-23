from django.urls import path 
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path ('authorised', views.AuthorisedView.as_view()),
       
]