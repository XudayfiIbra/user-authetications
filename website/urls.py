from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('logout/', views.logout_user, name="logout_user"),
    path('posts/', views.posts, name="postPage"),
    path('singup/', views.user_register, name="singup")
]
