from django.urls import path
from .views import *

app_name = 'writers'

urlpatterns = [
    path('mypage/<int:id>', mypage, name='mypage'),
    path('post_epilogue/<int:worry_id>', post_epilogue, name='post_epilogue'),
]