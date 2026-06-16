from django.db import models

class Worry(models.Model):
    keyword = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    content = models.TextField()
    mbti = models.CharField(max_length=4)
    pub_date = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_HoF = models.BooleanField(default=False)
    cheerup = models.PositiveIntegerField(default=0)
    gonggam = models.PositiveIntegerField(default=0)

    # 20자 넘기면 ... 붙이고 요약
    def summary(self):
        str = self.content
        if len(self.content) > 20:
            str = str[:20] + "..."
        return str
