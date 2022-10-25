from django.contrib import admin
from .models import UserModel


admin.site.register(UserModel) # UserModel을 Admin페이지에 추가
