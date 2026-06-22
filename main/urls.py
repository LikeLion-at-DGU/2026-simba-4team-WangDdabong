from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', demo_home, name = 'demo_home'),
    path("daily_attend/", daily_attend, name="daily_attend"),
    path("get_yang_store/", get_yang_store, name="get_yang_store"),
    path("post_buy_yang/<str:yang_id>", post_buy_yang, name="post_buy_yang"),
]