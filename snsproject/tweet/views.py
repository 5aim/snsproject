from django.shortcuts import render, redirect
from .models import TweetComment, TweetModel
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView # 태그기능


# 홈화면
def home(request):
    user = request.user.is_authenticated
    # 사용자가 로그인 했는지 확인해서 페이지를 나눠보여주도록 함

    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


# 게시글 불러오기와 작성
def tweet(request):
    # 게시글 불러오기
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at') # 작성글 모두 최근 작성 순으로 불러오고
            return render(request, 'tweet/home.html', {'tweet':all_tweet}) # tweet으로 데이터를 모두 담는다.
        else:
            return redirect('/sign-in')

    # 게시글 작성
    elif request.method == 'POST':
        user = request.user
        content = request.POST.get('my-content', '')
        tags = request.POST.get('tag','').split('#')

        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'error':'글을 작성해주세요', 'tweet':all_tweet})

        else:
            my_tweet = TweetModel.objects.create(author=user, content=content)

        # 아래와 위에 else문의 저장 방식 비교 !!
        # my_tweet = TweetModel()
        # my_tweet.author = user
        
        # # home.htm에 id = my-content. POST형식으로 요청한 데이터를 id, name으로 가져올 수 있음
        # my_tweet.content = request.POST.get('my-content', '')

            for tag in tags:
                tag = tag.strip()

                if tag != '': # 태그를 작성하지 않았을 경우 not save
                    my_tweet.tags.add(tag)

        my_tweet.save()
        return redirect('/tweet')


# 글 삭제.
@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


# 댓글 불러오기
@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet':my_tweet, 'comment':tweet_comment})


# 댓글 작성
@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))


# 댓글 삭제
@login_required
def delete_comment(requeset, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))


# 태그를 모아두는 태그 클라우드
class TagCloudTV(TemplateView):
    template_name = 'greenlight/tag_cloud_view.html'


# 태그를 모아서 화면에 전달하는 역할
class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context