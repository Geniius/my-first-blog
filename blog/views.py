from django.shortcuts import render
from django.utils import timezone
from .models import Post



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# ############## Урок по Django 1
# from django.http import HttpResponse
# from django.template.loader import get_template, render_to_string
# from . import models
#
# def hello_world(request):
#     query = models.Product.objects.all()
#     return render(request, 'products/index.html', {'results' : query, 'user' : request.user})