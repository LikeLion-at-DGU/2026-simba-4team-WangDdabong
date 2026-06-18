from django.contrib.auth.models import User
from django.shortcuts import render, redirect , get_object_or_404
from accounts.models import Profile
from worries.models import Worry

# Create your views here.

"""
    [마이페이지 함수]
    - 기능 : 내 정보, 내 활동 정보들 한눈에 리스트 확인 가능
    - 가져오는 정보 : User, Profile
    - 연결 페이지 : 양 성장과정 구매, 내 고민, 내 답변, 포인트 이용내역, 북마크
    - return : mypage.html 화면 표시
    * 유의사항 : 로그인 하지 않고 마이페이지 들어가면 로그인 페이지로 넘어감 *
"""

def mypage(request):

    if not request.user.is_authenticated:
        return redirect("accounts:login")   # 비로그인 시, 로그인 페이지로 넘어감

    profile = get_object_or_404(Profile, writer=request.user)

    context = {
        'profile_writer' : request.user,
        'profile' : profile,
    }

    return render(request, 'writers/mypage.html', context)


"""
    [내 고민 함수]
    - 기능 : 본인이 작성한 고민들 고민배송중/공개O/공개X 로 나누어서 볼 수 있음
    - 가져오는 정보 : Worry
    - return : demo_my_worry.html 화면 표시
"""

def my_worry(request):
    
    if not request.user.is_authenticated:
        return redirect("accounts:login")   # 비로그인 시, 로그인 페이지로 넘어감

    delivery_worries = Worry.objects.filter(    # 고민 배송 중
        writer = request.user,
        is_complete = False
    )
    public_worries = Worry.objects.filter(      # 공개 O
        writer = request.user, 
        is_complete = True, 
        is_HoF=True
    )
    private_worries = Worry.objects.filter(     # 공개 X
        writer = request.user,
        is_complete = True,
        is_HoF = False
    )

    context = {
        'delivery_worries' : delivery_worries,
        'public_worries' : public_worries,
        'private_worries' : private_worries,
    }

    return render(request, 'writers/demo_my_worry.html', context)


"""
    [내 답변 함수]
    - 기능 : 본인이 작성한 답변들을 볼 수 있음
    - 가져오는 정보 : 
    - return : demo_my_answer.html 화면 표시
"""

def my_answer(request):

    if not request.user.is_authenticated:
        return redirect("accounts:login")   # 비로그인 시, 로그인 페이지로 넘어감

    return render(request, 'writers/demo_my_answer.html')


"""
    [북마크 함수]
    - 기능 : 본인이 작성한 답변들을 볼 수 있음
    - 가져오는 정보 : Worry
    - return : demo_bookmark.html 화면 표시
    * 유의사항 : 현재 후일담 북마크가 없어서 고민 북마크만 넣어둠. 추후에 반영 예정 *
"""

def bookmark(request):

    if not request.user.is_authenticated:
        return redirect("accounts:login")   # 비로그인 시, 로그인 페이지로 넘어감
    
    worry_bookmarks = Worry.objects.filter(later_answer = request.user.id)     # 고민 북마크

    context = {
        'worry_bookmarks' : worry_bookmarks,
    }

    return render(request, 'writers/demo_bookmark.html', context)