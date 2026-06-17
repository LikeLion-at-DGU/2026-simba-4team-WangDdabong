from django.shortcuts import render, redirect, get_object_or_404
from .models import *

"""
[고민 작성]
- 기능: 작성한 내용으로 Worry 객체 생성 및 저장
- 받는 값: keyword, title, content, mbti
- return: 성공 -> demo_home 리다이렉트 / 실패(인증 에러) -> 로그인 메서드로 리다이렉트
"""
def write_worry(request):
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