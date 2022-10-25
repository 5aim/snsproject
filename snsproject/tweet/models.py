# tweet/models.py
from django.db import models
from user.models import UserModel # user앱에 있는 models


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
		# ForeignKey : UserModel을 가져와서 사용하겠다
		# author는 새로운 사람이 아니라 아까 만들어 주었던
		# User Model의 사용자가 작성 한 글 이기 때문에
		# ForeignKey를 사용해서 넣어주는것임.

    content = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)