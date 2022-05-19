from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from accounting.forms import LoginForm
from django.contrib import messages


def home(request):
    return render(request, 'accounting/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'\"{form.cleaned_data["username"]}\" was successfully created.'
            )
            return redirect('login')

    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounting/register.html', context)


def login_user(request):
    form = LoginForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get('username')
            password = cd.get('password')
            obj = authenticate(request, username=username, password=password)
            if obj:
                login(request, obj)
                messages.success(request, 'You are successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials.')
    return render(request, 'accounting/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
