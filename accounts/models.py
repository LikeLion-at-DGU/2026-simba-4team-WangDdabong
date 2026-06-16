from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.

class Profile(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    # bookmark_for_answer = models.ForeignKey('main.WorryPost',on_delete = models.SET_NULL, null = True, blank = True)
    # epilogue = models.ForeignKey('main.Epilogue', on_delete = models.SET_NULL, null = True, blank = True)
    signup_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 20)        #이름
    mbti = models.CharField(max_length = 4)         #성향
    email = models.EmailField()                     #이메일
    point = models.IntegerField(default = 0)        #포인트 및 카운트
    worry_count = models.IntegerField(default = 0)
    worry_yang = models.IntegerField(default = 0)

    def __str__(self):
        return self.writer.username