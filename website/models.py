from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.CharField(max_length=10000)
    heading = models.CharField(max_length=1000)
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()
    paragraph_three = models.TextField()
    paragraph_four = models.TextField()
    post_published = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    creater = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-post_published']
    
    
