from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=80)

    def __str__(self):
        return f'{self.user.username} Profile'
