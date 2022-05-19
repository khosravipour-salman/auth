from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'accounting/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and email and password1 and password2:
            if not User.objects.filter(username=username).exists():
                if password1 == password2:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1,
                    )
                    return redirect('login')

                else:
                    context = {
                        'message': 'Passwords does not match!',
                    }
                    return render(request, 'accounting/register.html', context)

            else:
                context = {
                    'message': 'This username is already taken.',
                }
                return render(request, 'accounting/register.html', context)

        else:
            context = {
                'message': 'Make sure to fill out all the form fields!',
            }
            return render(request, 'accounting/register.html', context)

    return render(request, 'accounting/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(
            request,
            username=username,
            password=password,
        )
        if obj:
            login(request, obj)
            return redirect('home')
        else:
            context = {
                'message': 'Invalid username or password.'
            }
            return render(request, 'accounting/login.html', context)

    return render(request, 'accounting/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
