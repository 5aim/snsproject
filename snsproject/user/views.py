from django.shortcuts import HttpResponse, redirect, render
from .models import UserModel
from django.contrib.auth import get_user_model  # 회원가입 중복확인


# user/views.py

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

        else:
            exist_user = get_user_model().objects.filter(username=username)
            # username과 입력한 username이 같다면 exist_user로 저장하고
            # 위에 import한 get_user_model함수를 사용해서 데이터베이스에 있는지 없는지 중복확인을 해주고

            if exist_user:
                return render(request, 'user/signup.html')
                # 사용자가 존재하면 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움

            else:
                UserModel.objects.create_user(
                    # 중복이 아닌 경우 바로 유저를 생성해서 저장해줌.
                    username=username, password=password, bio=bio)
                return redirect('/sign-in')  # 회원가입이 완료되었으므로 로그인 페이지로 이동


def sign_in_view(request):
    if request.method == 'GET':
        return render(request, 'user/signin.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = UserModel.objects.get(username=username)  # 사용자 불러오기

        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return HttpResponse(me.username)  # 로그인 성공 문구를 사용자 이름으로 변경

        else:  # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/sign-in')
