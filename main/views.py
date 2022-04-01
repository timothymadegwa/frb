from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def wallet(request):
    return render(request, 'main/wallet.html')
