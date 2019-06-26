from django.shortcuts import render
from . models import Post

def home(request):
    context = {}
    return render(request, 'home/home.html', context)

def about(request):
    context = {'title':'About'}
    return render(request, 'home/about.html', context)

def blog(request):
    context = {'title':'Blog', 'posts': Post.objects.all()}
    return render(request, 'home/blog.html', context)