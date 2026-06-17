from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("worry_write/", views.worry_write, name="worry_write"),
    path("worry_list/", views.worry_list, name="worry_list"),
    path("worry_detail/", views.worry_detail, name="worry_detail"),
    path("worry_reply/", views.worry_reply, name="worry_reply"),
]