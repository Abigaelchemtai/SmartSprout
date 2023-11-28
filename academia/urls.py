from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('navigation/', views.navigation, name='navigation'),
    path('services/', views.services, name='services'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.ContactUs, name='contact'),
    path('order/', views.CreateOrder, name='order')

]
