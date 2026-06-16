from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def signup(request): 
    """
    [회원가입 함수]
    - 기능 : 유저 정보, 프로필 정보를 받아 회원가입시킨 후, 자동 로그인 처리
    - 받는 값 : username, password, confirm, mbti, email
    - return : 성공 -> demo_home로 이동 / 실패 -> signup.html 화면 표시
    """
    if request.method == 'POST': #사용자가 화면에서 '회원가입' 버튼을 눌러 데이터를 전송한 경우(처리 시작)
        if request.POST['password'] == request.POST['confirm']:

            username = request.POST['username']
            name = request.POST['name']
            mbti = request.POST['mbti']
            email = request.POST['email']

            if User.objects.filter(username=username).exists():
                return render(
                    request, 'accounts/demo_signup.html', {'message' : '이미 사용 중인 아이디입니다.'}
                )

            if Profile.objects.filter(email=email).exists():
                return render(
                    request, 'accounts/demo_signup.html', {'message' : '이미 사용 중인 이메일입니다.'}
                )


            newwriter = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )

            profile = Profile(
                writer=newwriter,
                name = name,
                mbti = mbti,
                email = email,
            )

            profile.save()

            auth.login(request, newwriter) #로그인 상태 유지 및 로그인 처리 완료
            return redirect('main:demo_home')  #main:demo_firstpage 메인 첫 화면 url 로 이동
        
    return render(request, 'accounts/demo_signup.html') #주소를 치고 들어왔을 때 or 회원가입에 실패헀을 때
                                                        ##accounts/templates/accounts/demo_signup.html 로 이동

def login(request):
    """
    [로그인 함수]
    - 기능 : 아이디와 비밀번호 검증 후 로그인 처리
    - 받는 값 : username, password
    - return : 성공 -> demo_home로 이동 / 실패 -> login.html 화면 표시
    """
    if request.method == 'POST': #사용자가 화면에서 '로그인' 버튼을 눌러 데이터를 전송한 경우(처리 시작)
        username = request.POST['username']
        password = request.POST['password']

        writer = auth.authenticate(request, username=username, password=password)

        if writer is not None:  #로그인 성공한 경우
            auth.login(request, writer)
            return redirect('main:demo_home') #메인:첫화면 주소 반환
        else:
            return render(request, 'accounts/demo_login.html') #accounts/templates/accounts/demo_login.html 로 이동
        
    elif request.method == 'GET': #로그인하러 가기 버튼을 눌렀을 때 or 주소창에 주소를 치고 들어왔을 때
        return render(request, 'accounts/demo_login.html') #accounts/templates/accounts/demo_login.html 로 이동
    

def logout(request):
    """
    [로그아웃 함수]
    """
    auth.logout(request) #로그아웃을 눌렀을 때
    return redirect('main:demo_home') #main:demo_firstpage 메인 첫 화면 url 로 이동