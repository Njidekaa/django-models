from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here. 

class Post(models.Model):
    title = models.CharField(max_length= 200, unique=True)
    text= models.TextField(max_length= 250, unique=True)
    author= models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    created_date= models.DateTimeField()
    published_date= models.DateTimeField(default=timezone.now)
