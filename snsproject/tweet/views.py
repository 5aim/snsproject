from django.shortcuts import render, redirect
from .models import TweetModel

# 사용자가 로그인 했는지 확인해서 페이지를 나눠보여주도록 함
def home(request):
    user = request.user.is_authenticated

    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


# tweet에 home띄워주기
def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return render(request, 'tweet/home.html')
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        user = request.user

        my_tweet = TweetModel()
        my_tweet.author = user
        # home.htm에 id = my-content. POST형식으로 요청한 데이터를 id, name으로 가져올 수 있음
        my_tweet.content = request.POST.get('my-content', '')

        my_tweet.save()
        return redirect('/tweet')