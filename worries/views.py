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
- 기능: 고민글에 대해 북마크를 추가
- 받는 값: worry_id
- return: 성공 시 -> 기존 화면(고민 리스트)으로 리다이렉트
""" 
def post_bookmark(request, worry_id):
    worry = get_object_or_404(Worry, pk=worry_id)

    if request.user in worry.later_answer.all():
        worry.later_answer.remove(request.user)
        worry.save()
    else:
        worry.later_answer.add(request.user)
        worry.save()

    return redirect("worries:get_worries")

def post_cheerup(request, worry_id):
    worry = get_object_or_404(Worry, pk=worry_id)

    if request.user in worry.cheerup.all():
        worry.cheerup.remove(request.user)
        worry.cheerup_count -= 1
        worry.save()
    else:
        worry.cheerup.add(request.user)
        worry.cheerup_count += 1
        worry.save()

def get_worry_detail(request, worry_id):
    worry = get_object_or_404(Worry, pk=worry_id)

    return render(request, "worries/demo_worry_detail.html", {"worry": worry})