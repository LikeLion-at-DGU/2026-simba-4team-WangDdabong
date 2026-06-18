from django.db import models
from django.contrib.auth.models import User

"""
고민
6/17 : writer FK 수정으로 인한 models.py 수정. db 삭제했다가 다시 만듦.
"""
class Worry(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)                          # 작성한 사용자 정보
    keyword = models.CharField(max_length=20)                                           # 키워드
    title = models.CharField(max_length=50)                                             # 제목
    content = models.TextField()                                                        # 본문
    mbti = models.CharField(max_length=4)                                               # 선호 MBTI
    pub_date = models.DateField(auto_now_add=True)                                      # 생성일
    is_delete = models.BooleanField(default=False)                                      # 삭제 여부
    is_complete = models.BooleanField(default=False)                                    # 완료 여부
    is_HoF = models.BooleanField(default=False)                                         # 명예의 전당 등재 여부
    cheerup = models.ManyToManyField(User, related_name="worry_cheerup", blank=True)    # 응원 도장
    cheerup_count = models.PositiveIntegerField(default=0)                              # 응원 도장 개수
    gonggam = models.ManyToManyField(User, related_name="worry_gonggam", blank=True)    # 공감 도장
    gonggam_count = models.PositiveIntegerField(default=0)                              # 공감 도장 개수
    later_answer = models.ManyToManyField(User, related_name="worry_later_answer", blank=True) # 나중에 답변할 고민 북마크

    # 20자 넘기면 ... 붙이고 요약
    def summary(self):
        str = self.content
        if len(self.content) > 20:
            str = str[:20] + "..."
        return str
