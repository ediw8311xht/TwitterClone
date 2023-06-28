from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text
