from django.shortcuts import render
from django.utils import timezone
from .models import Post
<<<<<<< HEAD
# from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> b4d9de804ba72fd6be89302ce17e50fe533797ec
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/base_reserv.html', {'posts': posts})

def freelance(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



# ############## Урок по Django 1
# from django.http import HttpResponse
# from django.template.loader import get_template, render_to_string
# from . import models
#
# def hello_world(request):
#     query = models.Product.objects.all()
#     return render(request, 'products/index.html', {'results' : query, 'user' : request.user})