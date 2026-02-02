from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.authtoken.models import Token



User = get_user_model()

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if not email:
            messages.error(request, "Email не может быть пустым")
            return redirect('register')

        if password != password2:
            messages.error(request, "Пароли не совпадают")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует")
            return redirect('register')


        user = User.objects.create_user(email=email, password=password)
        messages.success(request, "Регистрация успешна! Теперь войдите в систему.")
        return redirect('login')

    return render(request, "auth/register.html")



def login_custom(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)

            return redirect("index")
        else:
            messages.error(request, "Неверное имя пользователя или пароль")

    return render(request, "auth/login.html")

