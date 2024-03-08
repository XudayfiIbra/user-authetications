from django.contrib import admin
from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'body','creater','created_date', 'post_published',)
    list_filter = ('post_published',)
    prepopulated_fields = {"slug": ("post_title",)}


admin.site.register(Post, PostAdmin)
