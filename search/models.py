from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImageResult(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=18)
    portrait = models.BooleanField(default=False)
    bw = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)