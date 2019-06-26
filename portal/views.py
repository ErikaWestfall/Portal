from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request, username=None):
    u = request.user
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user

    args = {'user': user, 'title': f'{user}', 'u': u}

    return render(request, 'portal/profile.html', args)