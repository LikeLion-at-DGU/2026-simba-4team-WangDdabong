from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile, Attendance
from writers.models import PointLog
from worries.models import Worry
from .utils import TODAY_MESSAGES
from django.utils import timezone
from datetime import timedelta
import random

"""
[홈 화면]
- 기능: 홈 화면 렌더링
- 받는 값 : source
- return: 성공 -> home 렌더링
"""
def home(request, source="DONT_CARE"):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    today = timezone.now().date()
    profile = get_object_or_404(Profile, writer=request.user)

    # 출석 체크 가능 여부 검사
    current_week_start = today - timedelta(days=today.weekday())  # 이번 주 월요일 날짜
    current_week_end = current_week_start + timedelta(days=6)    # 이번 주 일요일 날짜

    weekly_attendance = Attendance.objects.filter( # 이번 주 출석 기록
        writer=request.user,
        date__range=(current_week_start, current_week_end)
    )

    weekly_attendance_weekdays = []
    for attendance in weekly_attendance:
        weekly_attendance_weekdays.append(attendance.date.weekday())

    show_attendance_popup = today.weekday() not in weekly_attendance_weekdays # 오늘 요일이 이번 주 출석 기록에 없으면 팝업 출력

    # 상단 남은 고민 개수, 남은 포인트
    worry_count = profile.worry_count
    points = profile.points

    # 최신 고민 5개 추출
    now_worries = Worry.objects.filter(
        is_delete = False
    ).order_by("-pub_date")[:5]

    # 오늘의 멘트 선정
    today_message = random.choice(TODAY_MESSAGES)

    # 후일담 작성 화면에서 왔다면 팝업 출력
    show_epilogue_popup = (source == "post_epilogue")

    context = {
        "worry_count": worry_count,
        "points": points,
        "now_worries": now_worries,
        "today_message": today_message,
        "show_epilogue_popup": show_epilogue_popup,
        "show_attendance_popup": show_attendance_popup,
    }

    return render(request, 'main/home.html', context)

"""
[출석 체크]
- 기능: 출석체크 기능. 포인트 증감 함수 이용
- 받는 값: X
- return: 성공 시 -> 홈 화면 리다이렉트
"""
def daily_attend(request):
    print("daily_attend 진입")
    if not request.user.is_authenticated:
        print("로그인 안됨")
        return redirect("accounts:login")

    if request.method != "POST":
        return redirect("main:home")

    profile = get_object_or_404(Profile, writer=request.user)
    today = timezone.now().date()

    current_week_start = today - timedelta(days=today.weekday())  # 이번 주 월요일 날짜
    current_week_end = current_week_start + timedelta(days=6)    # 이번 주 일요일 날짜

    # 오늘 출석 여부 검사
    today_attendance = Attendance.objects.filter(
        writer=request.user,
        date=today
    )
    if today_attendance.exists():
        return redirect("main:home")

    new_attendance = Attendance()   # 오늘 출석 안 했으면 출석 기록 생성
    new_attendance.writer = request.user
    new_attendance.date = today
    new_attendance.save()

    # 기본 출석
    edit_points(profile, "출석", 1)
    profile.last_attendance = today

    # 보너스 점수 검사 (일주일 모두 출석)
    weekly_attendance_count = Attendance.objects.filter(
        writer=request.user,
        date__range=(current_week_start, current_week_end)
    ).count()

    if weekly_attendance_count == 7:    # 일주일 모두 출석
        edit_points(profile, "일주일 출석 보너스", 3)                      # 보너스(3) + 출석(1) = 4

    # 마지막 출석 정보 최신화
    profile.last_attendance = today
    profile.attendance_count += 1
    profile.save()

    return redirect("main:home")

"""
[포인트 증감 함수]
- 기능: profile 객체의 포인트를 points 만큼 증감
"""
def edit_points(profile, source, amount):
    if amount >= 0:
        point_type = "EARN"
    else:
        point_type = "USE"
    
    # 잔액 부족시
    if profile.points + amount < 0:
        return

    profile.points += amount
    profile.save()

    point_log = PointLog()
    point_log.writer = profile.writer
    point_log.point_type = point_type
    point_log.source = source
    point_log.amount = amount
    point_log.points_after = profile.points

    point_log.save()
