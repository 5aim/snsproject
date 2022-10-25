#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# class 상속 : AbstractUser에서 사용하는 기능들을 UserModel에서도 사용할 수 있도록
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user" # Table name

    # Table > object
    bio = models.TextField(max_length=500, blank=True)