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
            auth_login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials")
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
                messages.error(request, "Email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    full_name=name,
                    email=email,
                    password=password,
                )
                user.save()
                auth_login(request, user)
                messages.success(request, "User created")
                return redirect("home")
        else:
            messages.error(request, "Password not matching")
            return redirect("register")
    return render(request, "users/register.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")
