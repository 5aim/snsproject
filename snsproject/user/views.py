from django.shortcuts import HttpResponse, redirect, render
from .models import UserModel
from django.contrib.auth import get_user_model  # 회원가입 중복확인
from django.contrib import auth  # 사용자 auth 기능
from django.contrib.auth.decorators import login_required

# 회원가입
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html', {'error': '비밀번호가 같지 않습니다. 다시 확인해주세요.'})

        else:
            if username == '' or password == '' :
                return render(request, 'user/signup.html', {'error':'아이다와 비밀번호는 필수입니다.'})
            exist_user = get_user_model().objects.filter(username=username)
            # username과 입력한 username이 같다면 exist_user로 저장하고
            # 위에 import한 get_user_model함수를 사용해서 데이터베이스에 있는지 없는지 중복확인을 해주고

            if exist_user:
                return render(request, 'user/signup.html', {'error':'이미 회원가입된 사용자입니다.'})
                # 사용자가 존재하면 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움

            else:
                UserModel.objects.create_user(
                    # 중복이 아닌 경우 바로 유저를 생성해서 저장해줌.
                    username=username, password=password, bio=bio)
                return redirect('/sign-in')  # 회원가입이 완료되었으므로 로그인 페이지로 이동


# 로그인
def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated # 사용자가 로그인되어 있는지 검사

        if user:
            return redirect("/")
        else:
            return render(request, 'user/signin.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

		# 사용자 비밀번호와 유저네임이 맞는지 한번에 확인해주는 auth.authenticate
        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기

        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교 / 사용자가 있는지 없는지만 구분해주면 됨.
            auth.login(request, me) # 만약에 사용자가 비어있지 않으면 me 정보를 넣고서 로그인 시켜줌.
            return redirect('/')

        else:  # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return render(request, 'user/signin.html', {'error':'아이디와 비밀번호를 확인해주세요'})


@login_required # == user = request.user.is_authenticated
def logout(request):
    auth.logout(request) # 인증되어 있는 정보를 없애줌.
    return redirect ('/')