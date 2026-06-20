from django.urls import path
from .views import *

app_name = 'writers'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
    path('my_worry/', my_worry, name='my_worry'),
    path('my_answer/', my_answer, name='my_anser'),
    path('bookmark/', bookmark, name='bookmark'),
    path('post_epilogue/<int:worry_id>', post_epilogue, name='post_epilogue'),
]