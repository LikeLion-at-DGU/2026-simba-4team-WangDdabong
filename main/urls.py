from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name = 'home'),
    path("daily_attend/", daily_attend, name="daily_attend")
]