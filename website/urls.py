from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('logout/', views.logout_user, name="logout_user"),
    path('posts/', views.posts, name="postPage"),
    path('singup/', views.user_register, name="singup"),
    path('post-reading/', views.post_reading, name="post_reading" ),
    path('add-post/', views.add_post, name="add_post"),
    path('delete-post/<int:id>', views.delete_post, name="delete_post")
]
