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