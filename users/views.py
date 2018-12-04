"""User views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

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
            {'message': 'Your registration was successful. Sign in for continue.'}
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


def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {'message': False, 'form':form})
