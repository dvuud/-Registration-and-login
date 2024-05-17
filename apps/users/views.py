from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким email не существует')
            return redirect('login')
        
        user_authenticated = authenticate(request, email=email, password=password)
        if user_authenticated is not None:
            if user_authenticated.is_active: 
                auth_login(request, user_authenticated)
                return redirect('home')
            else:
                messages.error(request, 'Ваш аккаунт заблокирован.')
        else:
            messages.error(request, 'Неправильный пароль')
    return render(request, 'pages/login.html', locals())

User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password == password2 and email:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Имя пользователя уже существует.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Эл. почта уже зарегистрирована.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти.')
                return redirect('login')
        else:
            messages.error(request, 'Неправильно введенный пароль или Эл. почта.')
    
    return render(request, 'pages/register.html',locals())