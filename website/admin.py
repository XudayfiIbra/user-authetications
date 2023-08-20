from django.contrib import admin
from . models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 
                    'slug', 
                    'image', 
                    'heading', 'paragraph_one',
                    'paragraph_two',
                    'paragraph_three',
                    'paragraph_four',
                    'creater',
                    'created_date',
                    )
    prepopulated_fields = {"slug": ("post_title",)}


admin.site.register(Post, PostAdmin)
