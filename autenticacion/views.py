from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

# Create your views here.


class CustomLoginView(SuccessMessageMixin, LoginView):
    success_url = 'home'
    success_message = 'Welcome to your profile'
