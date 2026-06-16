from django.urls import path
from .views import *

urlpatterns = [
    path('', demo_home, name = 'demo_home'),
]