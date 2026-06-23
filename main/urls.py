from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name = 'home'),
    path("post_epilogue/<int:epilogue_id>/", home_from_post_epilogue, name="home_from_post_epilogue"),

    path("daily_attend/", daily_attend, name="daily_attend"),
    path("go_epilogue/<int:epilogue_id>/", go_epilogue, name="go_epilogue"),
]