from django.shortcuts import render, redirect
from .models import Post, Comment
from .form import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    post = Post.objects.all().order_by("-last_modified")

    context = {
        "posts": post,
    }

    return render(request, "grampost/home.html", context)

def add_post(request):
    pass

def post_detail(request):
    pass

def like(request):
    pass