from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUser as User
from django.contrib.auth import logout, authenticate, login as auth_login


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            messages.info(request, "Login successful")
            auth_login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    return render(request, "users/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    full_name=name,
                    email=email,
                    password=password,
                )
                user.save()
                auth_login(request, user)
                messages.info(request, "User created")
                return redirect("home")
        else:
            messages.info(request, "Password not matching")
            return redirect("register")
    return render(request, "users/register.html")


def signout(request):
    logout(request)
    return redirect("home")
