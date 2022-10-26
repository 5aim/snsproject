from django.shortcuts import render, redirect

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
        return render(request, 'tweet/home.html')

