from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    image = models.CharField(max_length=10000)
    content = models.TextField()
    post_published = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    creater = models.CharField(max_length=255)
    
    
