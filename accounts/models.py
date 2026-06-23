from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 20)                      #이름
    mbti = models.CharField(max_length = 4)                       #성향
    email = models.EmailField()                                   #이메일
    points = models.IntegerField(default = 0)                     #포인트 및 카운트
    worry_count = models.IntegerField(default = 0)
    worry_yang = models.IntegerField(default = 0)
    attendance_count = models.IntegerField(default = 0)           # 출석체크 카운트
    last_attendance = models.DateField(blank=True, null=True)     # 마지막 출석체크 날짜  

    def __str__(self):
        return self.writer.username
    
"""
[출석기록 모델]
"""
class Attendance(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()