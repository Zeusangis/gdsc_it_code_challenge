from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUser as User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.check_password(password):
                messages.info(request, 'Login successful')
                return redirect('login')
            else:
                messages.info(request, 'Password not matching')
                return redirect('login')
        else:
            messages.info(request, 'Email not found')
            return redirect('login')
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(full_name=(f"{first_name} {last_name}"),  email=email, password=password)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'users/register.html')