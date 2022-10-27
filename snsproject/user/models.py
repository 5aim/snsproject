#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# class 상속 : AbstractUser에서 사용하는 기능들을 UserModel에서도 사용할 수 있도록
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user" # Table name

    # Table > object
    bio = models.TextField(max_length=500, blank=True)

    # django에서 사용할 user model은 setting.py에 AUTH_USER_MODEL로 선언되어있고
    # 위에 설정된 것을 setting.py로 직접 불러 오는 것이 아니라 setting하는 파일을 여러개로 나누어서 적용하는 것임.
    # 필요한 상황마다 장고가 알아서 settings.py을 가져오는 기능임.
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')