from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    path('announcements/', views.profile, name='SoM-announcements'),
    path('events/', views.profile, name='SoM-events'),
    path('profile/', views.profile, name='SoM-forum'),
]