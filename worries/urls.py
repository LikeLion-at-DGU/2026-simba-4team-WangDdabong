from django.urls import path
from .views import *

app_name = "worries"

urlpatterns = [
    path("post_worry/", post_worry, name="post_worry"),
    path("get_worries/", get_worries, name="get_worries"),
    path("post_bookmark/", post_bookmark, name="post_bookmark"),
    path("post_cheerup/", post_cheerup, name="post_cheerup"),
    path("get_worry_detail/", get_worry_detail, name="get_worry_detail"),
]