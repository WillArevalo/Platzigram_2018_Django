"""Posts Views"""

# Django
from django.shortcuts import render, redirect
# from django.http import HttpResponse

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    
    return render(request, 'posts/new.html', {'form':form})


def list_posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
    # return render(request,'template', {context})
    return render(request, 'posts/feed.html', {'posts': posts})
