from django.contrib import admin
from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'content', 'image', 'creater', 'created_date')


admin.site.register(Post, PostAdmin)
