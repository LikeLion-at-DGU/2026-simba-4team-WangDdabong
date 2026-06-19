from django.urls import path
from .views import *

app_name = "worries"

urlpatterns = [
    path("post_worry/", post_worry, name="post_worry"),
    path("get_worries/", get_worries, name="get_worries"),
    path("post_bookmark/<int:worry_id>", post_bookmark, name="post_bookmark"),
    path("post_cheerup/<int:worry_id>", post_cheerup, name="post_cheerup"),
    path("get_worry_detail/<int:worry_id>", get_worry_detail, name="get_worry_detail"),
    path("post_answer/<int:worry_id>", post_answer, name="post_answer"),
]