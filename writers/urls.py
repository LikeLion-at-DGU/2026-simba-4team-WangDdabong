from django.urls import path
from .views import *

app_name = 'writers'

urlpatterns = [
    path('mypage/', mypage, name='mypage'),
    path('my_worry/', my_worry, name='my_worry'),
    path('my_answer/<int:worry_id>', worry_story, {'source' : 'answer'}, name='my_answer'),
    path('my_answer_list/', my_answer_list, name='my_answer_list'),
    path('worry_bookmark/', worry_bookmark, name='worry_bookmark'),
    path('post_epilogue/<int:worry_id>', post_epilogue, name='post_epilogue'),
    path('ep_bookmark/<int:epilogue_id>', ep_bookmark, name='ep_bookmark'),
    path('post_epilogue_gonggam/<int:epilogue_id>', post_epilogue_gonggam, name='post_epilogue_gonggam'),
    path('worry_story/<int:worry_id>', worry_story, {'source' : 'worry'}, name='worry_story'),
    path('get_worry_answer/<int:worry_id>', get_worry_answer, name='get_worry_answer'),
]