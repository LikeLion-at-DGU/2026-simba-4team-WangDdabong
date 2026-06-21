from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', demo_home, name = 'demo_home'),
    path("daily_attend/", daily_attend, name="daily_attend")
]