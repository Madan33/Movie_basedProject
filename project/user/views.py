from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authlogin(request, user)
            return redirect('list')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def logout(request):
    authlogout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            error_message = 'Passwords do not match.'
            return render(request, 'signup.html', {'error_message': error_message})
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists. Please choose a different one.'
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            user = User.objects.create_user(username=username, password=password1)
            return redirect('login')
    return render(request, 'signup.html')
