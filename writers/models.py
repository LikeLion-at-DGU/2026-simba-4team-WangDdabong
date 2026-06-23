from django.db import models
from django.contrib.auth.models import User

"""
후일담
"""
class Epilogue(models.Model):
    worry = models.OneToOneField("worries.Worry", on_delete=models.CASCADE)                        # 관련된 고민
    writer = models.ForeignKey(User, on_delete=models.CASCADE)                                  # 고민, 후일담 작성자
    visible_users = models.ManyToManyField(User, related_name="visible_epilogue", blank=True)   # 해당 후일담을 조회할 수 있는 사용자들
    ep_han_madi = models.CharField(max_length=50)                                               # 한 마디
    ep_title = models.CharField(max_length=50)                                                  # 제목
    ep_content = models.TextField()                                                             # 내용
    ep_pub_date = models.DateField(auto_now_add=True)                                           # 작성일
    ep_is_delete = models.BooleanField(default=False)                                           # 삭제 여부
    later_check = models.ManyToManyField(User, related_name="ep_later_check", blank=True)       # 나중에 확인할 후일담 북마크
    ep_gonggam = models.ManyToManyField(User, related_name="ep_gonggam", blank=True)            # 후일담 공감 도장
    ep_gonggam_count = models.PositiveIntegerField(default=0)                                   # 후일담 공감 도장 개수

"""
포인트 이용내역
"""
class PointLog(models.Model):
    writer = models.ForeignKey(User, related_name="point_logs", on_delete=models.CASCADE)       # 사용자
    point_type = models.CharField(max_length=10)                                                # 포인트 변동 유형 (획득: 'EARN'/사용: 'USE)
    source = models.CharField(max_length=50)                                                    # 획득처/사용처
    amount = models.IntegerField()                                                              # 획득량(양수)/사용량(음수)
    points_after = models.IntegerField()                                                        # 획득/사용 후 잔액
    created_at = models.DateTimeField(auto_now_add=True)                                        # 이벤트 발생일