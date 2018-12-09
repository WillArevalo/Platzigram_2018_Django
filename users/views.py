"""User views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.models import User

# Forms
from users.forms import ProfileForm, SignupForm

# Models
from posts.models import Post

# Create your views here.


def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
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

            url = reverse('users:detail', kwargs={'username_slug': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(request, 'users/update_profile.html', {'message': False, 'form':form})


class UserDetailView(DetailView):
    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(profile__user=user).order_by('-created')
        return context


