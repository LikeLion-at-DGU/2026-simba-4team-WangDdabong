from django.db import models

"""
고민
"""
class Worry(models.Model):
    keyword = models.CharField(max_length=20)           # 키워드
    title = models.CharField(max_length=50)             # 제목
    content = models.TextField()                        # 본문
    mbti = models.CharField(max_length=4)               # 선호 MBTI
    pub_date = models.DateField(auto_now_add=True)      # 생성일
    is_delete = models.BooleanField(default=False)      # 삭제 여부
    is_complete = models.BooleanField(default=False)    # 완료 여부
    is_HoF = models.BooleanField(default=False)         # 명예의 전당 등재 여부
    cheerup = models.PositiveIntegerField(default=0)    # 응원 도장 개수
    gonggam = models.PositiveIntegerField(default=0)    # 공감 도장 개수

    # 20자 넘기면 ... 붙이고 요약
    def summary(self):
        str = self.content
        if len(self.content) > 20:
            str = str[:20] + "..."
        return str
