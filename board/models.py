from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='likes', blank=True)  # 다대다 관계 어떤모델과 보드모델이 다대다인지
#     다대다 관게는 class가 아니라 새로운 테이블이 추가됨
#  desc board_board; 안에는 안보이지만 show table;하면 보임