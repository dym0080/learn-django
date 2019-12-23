from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# on_delete 在2.0后是必选参数。

class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=300)
    last_update = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Post(models.Model):
    message = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)