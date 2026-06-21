from django.db import models
from django.contrib.auth.models import User

"""
후일담
"""
class Epilogue(models.Model):
    worry = models.ForeignKey("worries.Worry", on_delete=models.CASCADE)                # 관련된 고민
    writer = models.ForeignKey(User, on_delete=models.CASCADE)                          # 고민, 후일담 작성자
    ep_han_madi = models.CharField(max_length=50)                                       # 한 마디
    ep_title = models.CharField(max_length=50)                                          # 제목
    ep_content = models.TextField()                                                     # 내용
    ep_pub_date = models.DateField(auto_now_add=True)                                   # 작성일
    ep_is_delete = models.BooleanField(default=False)                                   # 삭제 여부