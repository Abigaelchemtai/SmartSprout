from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Orders, Contact


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ('name', 'price', 'product', 'phone', 'message')


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
