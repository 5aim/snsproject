from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    # id를 views.py의 delete_tweet(request,id)에서 매개변수로 받아 사용

    path('tweet/<int:id>', views.detail_tweet, name='detail_tweet'),
    path('tweet/comment/<int:id>', views.write_comment, name='write_comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete_comment'),

    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>', views.TaggedObjectLV.as_view(), name='tagged_object_list')
]