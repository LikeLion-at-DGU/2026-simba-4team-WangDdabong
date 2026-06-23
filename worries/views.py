from django.shortcuts import render, redirect, get_object_or_404
from writers.models import Epilogue
from .models import *
from django.http import JsonResponse

"""
[고민 작성]
- 기능: 작성한 내용으로 Worry 객체 생성 및 저장
- 받는 값: keyword, title, content, mbti
- return: 성공 -> home 리다이렉트 / 실패(인증 에러) -> 로그인 메서드로 리다이렉트
"""
def post_worry(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    if request.method == "POST":
        new_worry = Worry()

        new_worry.writer = request.user
        new_worry.keyword = request.POST["keyword"]
        new_worry.title = request.POST["title"]
        new_worry.content = request.POST["content"]
        new_worry.mbti = request.POST["mbti"]

        new_worry.save()

        return redirect("main:home")

    return render(request, "worries/post_worry.html")

"""
[고민 리스트 조회]
- 기능: 모든 고민글을 반환
- 받는 값: X
- return: 모든 Worry 객체
"""
def get_worries(request):
    worries = Worry.objects.all()

    return render(request, "worries/list.html", {"worries": worries})

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

    return render(request, "worries/worry_detail.html", {"worry": worry})

"""
[고민 답변 작성]
- 기능: POST-고민 답변 작성 / GET-고민 답변 작성 화면 이동
- 받는 값: worry_id + (POST의 경우: situation, my_action, recommendation)
- return: GET 성공 시 -> 고민 답변 작성 화면 렌더링 / POST 성공 시 -> 메인 화면 리다이렉트 / 실패 시 -> 로그인 화면 이동
"""
def post_answer(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")

    worry = get_object_or_404(Worry, pk=worry_id)

    # 고민 답변 작성 후 제출
    if request.method == "POST":
        answer = Answer()
        answer.worry = worry
        answer.writer = request.user
        answer.situation = request.POST["situation"]
        answer.my_action = request.POST["my_action"]
        answer.recommendation = request.POST["recommendation"]

        answer.save()

        return redirect("main:home")

    # 고민 답변 작성 화면 이동
    else:
        context = {
            "answer_user": request.user,
            "worry_writer": worry.writer.profile,
            "worry": worry,
        }
        return render(request, "worries/write_answer.html", context)

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


"""
    [명예의 전당 진입 함수]
    - 기능 : 공감 수가 가장 많은 후일담 카드 조회
    - 받는 값 : Epilogue
    - return : hall_of_fame_card 함수로 이동
"""

def hall_of_fame_entry(request):

    top_epilogue = Epilogue.objects.filter(
        worry__is_HoF=True
    ).order_by('-ep_gonggam_count').first()

    if not top_epilogue:
        return redirect("worries:hall_of_fame")

    return redirect("worries:hall_of_fame_card", top_epilogue.id)


"""
    [명예의 전당 - 메인 & 일반 카드 함수]
    - 기능 : 명예의 전당에 공개된 고민, 답변, 후일담 카드로 조회
    - 받는 값 : Worry, Answer, Epilogue
    - return : demo_hof_card.html 화면 표시 
    * 유의사항 : 배우지 않은 문법들이 들어있지만 없으면 구현을 하지 못해서 넣었음 *
            + 공감 수 1등 후일담이면 메인 카드
            + 나머지는 일반 카드
            + 좌우 버튼으로 이전 or 다음 카드 이동 가능
            + 마지막 카드 다음은 메인 카드
            + 메인 카드 이전은 마지막 카드
"""

def hall_of_fame_card(request, epilogue_id):
    epilogue = get_object_or_404(Epilogue, pk=epilogue_id)

    worry = epilogue.worry

    answers = Answer.objects.filter(worry=worry)

    all_epilogues = list(
        Epilogue.objects.filter(
            worry__is_HoF=True
        ).order_by('-ep_gonggam_count')
    )

    current_index = all_epilogues.index(epilogue)

    is_main = (current_index == 0)

    prev_epilogue = all_epilogues[current_index - 1]

    next_epilogue = all_epilogues[(current_index + 1) % len(all_epilogues)]

    context = {
        'worry' : worry,
        'answers' : answers,
        'epilogue' : epilogue,
        'is_main' : is_main,
        'prev_epilogue' : prev_epilogue,
        'next_epilogue' : next_epilogue,
    }

    return render(request, 'worries/demo_hof_card.html', context)

def edit_satisfaction(request, answer_id, is_satisfied):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    answer = get_object_or_404(Answer, pk=answer_id)

    # 고민 작성자만 답변에 만족/불만족 가능
    if answer.worry.writer != request.user:
        return

    # 답변 만족/불만족 처리
    if (is_satisfied > 0): # 만족
        answer.is_satisfied = 1
    else: # 불만족
        answer.is_satisfied = -1

    answer.save()

    return redirect("writers:get_worry_answer", answer.worry.id)