from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name = "home"),
    path("new_post/", views.add_post, name = "add_post"),
    path("<int:pk>/", views.post_detail, name = "post_detail"),
    path("<int:pk>/", views.like, name = "likes"),
]