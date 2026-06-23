from django.utils import timezone

TODAY_MESSAGES = [
    "오늘은 어떤 고민을 전달해볼까요?",
    "소중한 고민이 깨지지 않게 배송할게요!",
    "오늘의 고민은 무엇인가요?",
]

"""
    [시간 계산 util 함수]
    - 기능: 현재 시간 기준 작성하고 얼마나 지났는지 계산
"""
def get_time_ago(pub_date):
    now = timezone.now()

    diff = now - pub_date
    seconds = diff.days * 24 * 60 * 60 + diff.seconds

    if seconds < 60:
        return "방금 전"

    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}분 전"

    hours = minutes // 60
    if hours < 24:
        return f"{hours}시간 전"

    days = hours // 24
    if days < 7:
        return f"{days}일 전"

    weeks = days // 7
    if weeks < 5:
        return f"{weeks}주 전"

    return str(pub_date.year) + "." + str(pub_date.month) + "." + str(pub_date.day)