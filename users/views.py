"""User views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.


def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        if passwd != passwd_confirmation:
            return render(
                request,
                'users/signup.html',
                {'error': 'Password confirmation does not match.'}
            )
        try:
            user = User.objects.create_user(
                username=username,
                password=passwd
            )
        except IntegrityError as e:
            return render(
                request,
                'users/signup.html',
                {'error': 'This username already exists. \n Try other'}
            )

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        profile = Profile(user=user)
        profile.save()

        return render(
            request,
            'users/login.html',
            {'message': 'Your registration was successful. \n Sign in for continue.'}
        )
    return render(request, 'users/signup.html', {'message': False})



def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'Invalid username or password.'}
            )
    return render(request, 'users/login.html')


def logout_view(request):
    """Logout view"""
    logout(request)
    return render(
        request,
        'users/login.html',
        {'message': 'Now, You are logout.'}
    )
