from django.shortcuts import render, redirect
from .models import TweetModel
from django.contrib.auth.decorators import login_required


def home(request):
    user = request.user.is_authenticated
    # 사용자가 로그인 했는지 확인해서 페이지를 나눠보여주도록 함

    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at') # 작성글 모두 최근 작성 순으로 불러오고
            return render(request, 'tweet/home.html', {'tweet':all_tweet}) # tweet으로 데이터를 모두 담는다.
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


# auth user가 필요하고 element로 id가 필요함.
@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')
