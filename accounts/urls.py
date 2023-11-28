
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signupPage, name='signup'),
    path('login/', LoginView.as_view(next_page='index'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

]