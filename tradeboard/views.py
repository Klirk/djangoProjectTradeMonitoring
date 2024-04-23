import logging

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

from database import APIWrapperDB as databaseApi

logger = logging.getLogger('django')


def first_page(request):
    return redirect('lending')


def logout_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return function(request, *args, **kwargs)

    return wrap


@logout_required
def lending_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, "lending.html")


@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")


@login_required
def settings_view(request):
    return render(request, "settings.html")

@login_required
def profile_view(request):
    return render(request, "profile.html")


def log_user_action(user, action):
    logger.info('User action occurred', extra={'user': user, 'action': action})


def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            log_user_action(request.user.username, "Login already exists")
            return JsonResponse({'answer': 'Login already exist', 'url': ''})
        else:
            # Your user creation logic here
            user = databaseApi.add_user(username, password)
            login(request, user[0])
            log_user_action(username, "User registered")
            return JsonResponse({'answer': 'Registration complete', 'url': '/dashboard/'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            log_user_action(username, "User logged in")
            return JsonResponse({'answer': 'Login success', 'url': '/dashboard/'})
        else:
            return JsonResponse({'answer': 'User not found', 'url': ''})


def logout_view(request):
    logout(request)
    return redirect('/lending/')
