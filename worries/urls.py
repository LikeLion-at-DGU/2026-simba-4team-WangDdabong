from django.urls import path
from .views import *

app_name = "worries"

urlpatterns = [
    path("write_worry/", write_worry, name="write_worry"),
]