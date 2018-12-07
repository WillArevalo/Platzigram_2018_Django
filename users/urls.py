"""Users URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Views
from users import views

urlpatterns = [

    # Management
    path(
        route='signup/',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout',
        view=login_required(views.logout_view),
        name='logout'
    ),
    path(
        route='me/profile/',
        view=login_required(views.update_profile),
        name='update_profile'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=login_required(TemplateView.as_view(template_name='users/detail.html')),
        name='detail'
    ),
]