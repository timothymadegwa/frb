from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile', views.profile, name = 'profile'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('wallet', views.wallet, name = 'wallet'),
    path('loans', views.loans, name = 'loans'),
    path('loans_due', views.loans_due, name = 'loans_due'),
    path('apply', views.apply, name = 'apply'),
]