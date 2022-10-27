# tweet/models.py
from django.db import models
from user.models import UserModel # user app > UserModel

# 게시글
class TweetModel(models.Model):
  class Meta:
      db_table = "tweet"

  author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
  # ForeignKey : UserModel을 가져와서 author와 연결시킴.
  # User Model의 사용자가 작성 한 글 이기 때문에 ForeignKey를 사용해서 넣어주는 것
  content = models.CharField(max_length=256)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# 댓글
class TweetComment(models.Model):
  class Meta:
    db_table = "comment"

  # 게시글(tweet)과 댓글 연결
  tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
  # author와 user를 연결
  author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
  comment = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)