from django.shortcuts import render, redirect, get_object_or_404
from .models import *

"""
[고민 작성]
- 기능: 작성한 내용으로 Worry 객체 생성 및 저장
- 받는 값: keyword, title, content, mbti
- return: 성공 -> demo_home 리다이렉트 / 실패(인증 에러) -> 로그인 메서드로 리다이렉트
"""
def post_worry(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    new_worry = Worry()

    new_worry.writer = request.user
    new_worry.keyword = request.POST["keyword"]
    new_worry.title = request.POST["title"]
    new_worry.content = request.POST["content"]
    new_worry.mbti = request.POST["mbti"]

    new_worry.save()

    return redirect("main:demo_home")

"""
[고민 리스트 조회]
- 기능: 모든 고민글을 반환
- 받는 값: X
- return: 모든 Worry 객체
"""
def get_worries(request):
    worries = Worry.objects.all()

    return render(request, "worries/demo_list.html", {"worries": worries})

"""
[고민 북마크 등록/취소]
- 기능: 나중에 답변할 고민 북마크를 추가/삭제
- 받는 값: worry_id
- return: 성공 시 -> 기존 화면(고민 리스트)으로 리다이렉트
""" 
def post_bookmark(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    worry = get_object_or_404(Worry, pk=worry_id)

    if request.user in worry.later_answer.all():
        worry.later_answer.remove(request.user)
        worry.save()
    else:
        worry.later_answer.add(request.user)
        worry.save()

    return redirect("worries:get_worries")

"""
[고민 응원 도장 등록/취소]
- 기능: 고민에 대해 응원 도장 추가/삭제
- 받는 값: worry_id
- return: 성공 시 -> 기존 화면(고민 리스트)으로 리다이렉트
"""
def post_cheerup(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    worry = get_object_or_404(Worry, pk=worry_id)

    if request.user in worry.cheerup.all():
        worry.cheerup.remove(request.user)
        worry.cheerup_count -= 1
        worry.save()
    else:
        worry.cheerup.add(request.user)
        worry.cheerup_count += 1
        worry.save()
    
    return redirect("worries:get_worries")

"""
[고민 상세 화면 리다이렉트]
- 기능: 고민 상세 화면으로 이동
- 받는 값: worry_id
- return: 성공 시 -> 고민 상세 화면으로 리다이렉트
"""
def get_worry_detail(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    worry = get_object_or_404(Worry, pk=worry_id)

    return render(request, "worries/demo_worry_detail.html", {"worry": worry})

"""
[고민 답변 작성]
- 기능: POST-고민 답변 작성 / GET-고민 답변 작성 화면 이동
- 받는 값: worry_id
- return: GET 성공 시 -> 고민 답변 작성 화면 렌더링 / POST 성공 시 -> 메인 화면 리다이렉트 / 실패 시 -> 로그인 화면 이동
"""
def post_answer(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    worry = get_object_or_404(Worry, pk=worry_id)
    # 고민 답변 작성 후 제출
    if request.method == "POST":
        # 고민 작성 기능 작업 필요
        return redirect(request, "main:home")
    # 고민 답변 작성 화면 이동
    else:
        return render(request, "worries/write_answer.html", {"answer_user": request.user, "worry_user": worry.writer})
    

"""
    [명예의 전당 리스트 함수]
    - 기능 : 명예의 전당에 공개된 고민들 리스트 조회
    - 받는 값 : Worry
    - return : demo_hof_list.html 화면 표시 
    * 유의사항 : 현재는 리스트만 구현. 추후 일반 카드와 메인 카드 구현 예정  *
"""

def hall_of_fame(request):
    
    hof_worries = Worry.objects.filter(is_HoF = True)   # 명예의 전당에 공개된 고민만 조회 가능

    context = {
        'hof_worries' : hof_worries,
    }

    return render(request, 'worries/demo_hof_list.html', context)