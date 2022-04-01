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

def loans(request):
    return render(request, 'main/loans.html')

def loans_due(request):
    return render(request, 'main/loans_due.html')

def apply(request):
    return render(request, 'main/apply.html')

def loan_requests(request):
    return render(request, 'main/loan_requests.html')
