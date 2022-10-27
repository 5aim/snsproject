from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    # id를 views.py의 delete_tweet(request,id)에서 매개변수로 받아 사용
]