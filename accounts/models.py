from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 20)                                #이름
    mbti = models.CharField(max_length = 4)                                 #성향
    email = models.EmailField()                                             #이메일
    points = models.IntegerField(default = 3)                               #포인트 및 카운트
    worry_count = models.IntegerField(default = 5)                          # 남은 고민 개수
    current_yang = models.CharField(max_length=50, default="new_yang")      # 현재 활성화 중인 워리양
    attendance_count = models.IntegerField(default = 0)                     # 출석체크 카운트
    last_attendance = models.DateField(blank=True, null=True)               # 마지막 출석체크 날짜  

    def __str__(self):
        return self.writer.username

    @property
    def answer_count(self):
        from worries.models import Answer

        return Answer.objects.filter(
            writer=self.writer,
            pub_date=timezone.now().date(),
        ).count()
    
    
"""
    [사용자가 갖고 있는 양]
"""
class UserYang(models.Model):
    writer = models.ForeignKey(User, related_name="have_yangs", on_delete=models.CASCADE)    # 사용자
    yang_id = models.CharField(max_length=50)
    purchased_at = models.DateField(auto_now_add=True)

"""
[출석기록 모델]
"""
class Attendance(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
