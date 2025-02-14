# authuser/views.py

from django.shortcuts import render
from django.conf import settings

def get_context():    
    return {'api_base_url': settings.API_BASE_URL}

def login(request):
    return render(request, 'authuser/login.html', get_context())

def register(request):
    return render(request, 'authuser/register.html', get_context())

def activate(request):
    return render(request, 'authuser/activation.html', get_context())

def forgot_password(request):
    return render(request, 'authuser/forgot_password.html', get_context())

def home(request):
    return render(request, 'authuser/home.html', get_context())

def my_profile(request):
    return render(request, 'authuser/my_profile.html', get_context())

def profile(request):
    return render(request, 'authuser/profile.html', get_context())

def setting(request):
    return render(request, 'authuser/setting.html', get_context())


def change_email(request):
    return render(request, 'authuser/change_email.html', get_context())

def change_mobile(request):
    return render(request, 'authuser/change_mobile.html', get_context())

def change_password(request):
    return render(request, 'authuser/change_password.html', get_context())