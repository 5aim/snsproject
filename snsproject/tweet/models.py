# tweet/models.py
from django.db import models
from user.models import UserModel # user app > UserModel


class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
		# ForeignKey : UserModel을 가져와서 author와 연결시킴.
		# User Model의 사용자가 작성 한 글 이기 때문에 ForeignKey를 사용해서 넣어주는 것
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)