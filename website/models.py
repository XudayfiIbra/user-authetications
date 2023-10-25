from django.db import models
from ckeditor.fields import RichTextField



class Post(models.Model):
    post_title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.CharField(max_length=10000)
    body = RichTextField(blank=True, null=True, )
    post_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    creater = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-post_published']
    
    
