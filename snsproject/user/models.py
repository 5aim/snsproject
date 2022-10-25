#user/models.py
from django.db import models

# 모델 생성하기
class UserModel(models.Model): #클래스 이름
    class Meta: # DB정보를 Meta에 적어줌.
        db_table = "my_user" # 내 테이블 이름

    username = models.CharField(max_length=20, null=False) # 이름 - object
    password = models.CharField(max_length=256, null=False) # 비밀번호 - object
    bio = models.CharField(max_length=256, default='') # 소개글 - object
    created_at = models.DateTimeField(auto_now_add=True) # 생성일 - object
    updated_at = models.DateTimeField(auto_now=True) # 수정일 - object