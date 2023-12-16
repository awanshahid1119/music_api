from django.db import models
from users.models import UserProfile
# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
