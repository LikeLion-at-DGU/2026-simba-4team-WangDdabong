from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile, UserYang
from worries.models import Worry
from .utils import *
from django.utils import timezone
from datetime import timedelta
import random

"""
[홈 화면]
- 기능: 홈 화면 렌더링
- 받는 값 : source
- return: 성공 -> demo_home 렌더링
"""
def demo_home(request, source="DONT_CARE"):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    today = timezone.localdate()
    profile = get_object_or_404(Profile, writer=request.user)
    already_attendance = True

    # 출석 체크 가능 여부 검사
    if today != profile.last_attendance:
        already_attendance = False
        return redirect("main:daily_attend")

    # 상단 남은 고민 개수, 남은 포인트
    worry_count = profile.worry_count
    points = profile.points

    # 최신 고민 5개 추출
    now_worries = Worry.objects.filter(
        is_delete = False
    ).order_by("-pub_date")[:5]

    # 오늘의 멘트 선정
    today_message = random.choice(TODAY_MESSAGES)

    # 팝업 출력 여부
    is_popup = False
    # 후일담 작성 화면에서 왔다면 팝업 출력
    if source == "post_epilogue":
        is_popup = True

    context = {
        "worry_count": worry_count,
        "points": points,
        "now_worries": now_worries,
        "today_message": today_message,
        "is_popup": is_popup,
        "already_attendance": already_attendance,
    }

    return render(request, 'main/demo_home.html', context)

"""
[출석 체크]
- 기능: 출석체크 기능. 포인트 증감 함수 이용
- 받는 값: X
- return: 성공 시 -> 홈 화면 리다이렉트
"""
def daily_attend(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    profile = get_object_or_404(Profile, writer=request.user)
    today = timezone.localdate()

    # 중복 출석 방지 (직접 URL로 접근 방어 목적)
    if profile.last_attendance == today:
        return redirect("main:demo_home")

    current_week_start = today - timedelta(days=today.weekday()) # 이번 주 월요일 날짜
    if profile.last_attendance:
        last_attendance_week_start = profile.last_attendance - timedelta(days=profile.last_attendance.weekday()) # 마지막 출석 주차 월요일 날짜

        # 현재 주차와 마지막 출석 주차가 다르면 주간 출석 횟수 초기화
        if current_week_start != last_attendance_week_start:
            profile.attendance_count = 0

    else: # 가입 후 최초 출석
        profile.attendance_count = 0

    # 주간 출석 횟수 +1
    profile.attendance_count += 1
    points = 1
    source = "출석"

    # 일 출석 (보너스 점수 검사)
    if today.weekday() == 6:
        if profile.attendance_count == 7:    # 일주일 모두 출석
            points += 3                      # 보너스(3) + 출석(1) = 4
            source = "일주일 출석 보너스"
    
    edit_points(profile, source, points)              # 점수 반영
    profile.last_attendance = today           # 마지막 출석 날짜 최신화
    profile.save()

    return redirect("main:demo_home")

"""
    [양 성장 과정 구매 화면 렌더링]
    - 기능: 양 성장 과정 구매 화면을 출력
    - 받는 값: X
    - return: 성공 시 -> main/yang_store.html / 실패 시 -> 로그인 화면
"""
def get_yang_store(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    profile = get_object_or_404(Profile, writer=request.user)
    
    context = {
        "worry_count": profile.worry_count,
        "points": profile.points,
        "yangs": Yang,
    }

    return render(request, "main/demo_yang_store.html", context)

"""
    [양 성장 과정 구매 함수]
    - 기능: 양 성장 과정 구매 처리
    - 받는 값: 어떤 양 구매할 지(yang_id)
"""
def post_buy_yang(request, yang_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    if UserYang.objects.filter(writer=request.user, yang_id=yang_id).exists():
        return redirect("writers:get_yang_store")

    profile = get_object_or_404(Profile, writer=request.user)

    yang = Yang.get(yang_id)
    source = yang["name"] + "구매"
    edit_points(profile, source, -yang["price"])
    
    user_yang = UserYang()
    user_yang.writer = profile.writer
    user_yang.yang_id = yang_id
    user_yang.save()

    return redirect("writers:get_yang_store")