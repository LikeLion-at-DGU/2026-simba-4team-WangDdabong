from django.urls import path
from .views import *

app_name = 'writers'

urlpatterns = [
    path('mypage/<int:id>', mypage, name='mypage'),
    path('my_worry/', my_worry, name='my_worry'),
    path('my_answer/', my_answer, name='my_anser'),
]