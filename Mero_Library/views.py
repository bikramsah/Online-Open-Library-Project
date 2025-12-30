from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Home.forms import User



def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        user_auth = authenticate(request, username=uname, password=passwd)

        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, f"Welcome, {user_auth}")
            return redirect('Home:Home')
        else:
            messages.error(request, "Invalid login data...")

    res = {}
    return render(request, 'login.html', res)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, "Thank You for your visit...")
    return render(request, 'login.html')

@login_required(login_url='profile')
def user_profile(request):
    return render(request, 'Profile.html')

def user_register(request):
    res = {}
    return render(request, 'register.html', res)

