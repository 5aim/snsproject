from django.contrib import admin # admin tool을 사용할거고
from .models import UserModel # models.py를 불러올거고 그 중에서 UserModel을 가져올 것

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
