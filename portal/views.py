from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': f'{user}'}

    return render(request, 'portal/profile.html', context)

@login_required
def Announcements(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Announcements'}

    return render(request, 'portal/Announcements.html', context)

@login_required
def Events(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Events'}

    return render(request, 'portal/Events.html', context)

@login_required
def Forum(request, username=None):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Forum'}

    return render(request, 'portal/Forum.html', context)