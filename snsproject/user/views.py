from django.shortcuts import HttpResponse, redirect, render
from .models import UserModel


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
            # 패스워드가 같지 않다면 user/sign-up 페이지를 보여줌
            # 패스워드가 같다면 아래로

        else:
            exist_user = UserModel.objects.filter(username=username)
            
            if exist_user:
                return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save()

                return redirect('/sign-in')
                # redirect 함수를 이용해서, 저장 완료 되었다면 로그인 페이지 인 /sign-in url로 이동


def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)  # 사용자 불러오기

        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return HttpResponse(me.username) # 로그인 성공 문구를 사용자 이름으로 변경

        else: # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/sign-in')
