from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User

# Create your models here.
# on_delete 在2.0后是必选参数。

class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()
    
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
    subject = models.CharField(max_length=300)
    last_update = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)