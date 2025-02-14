# authuser/urls.py

from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),        
    path('register/', views.register, name='register'),
    path('activate/', views.activate, name='activate'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('login/', views.login, name='login'),    
    path('profile/', views.profile, name='profile'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('setting/', views.setting, name='setting'),
    path('change-email/', views.change_email, name='change_email'),    
    path('change-mobile/', views.change_mobile, name='change_mobile'),    
    path('change-password/', views.change_password, name='change_password'),
]
