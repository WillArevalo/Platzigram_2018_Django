"""Posts URLs"""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from posts import views


urlpatterns = [
    path(
        route='',
        view=login_required(views.PostFeedView.as_view()),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=login_required(views.create_post),
        name='create_post'
    ),
]
