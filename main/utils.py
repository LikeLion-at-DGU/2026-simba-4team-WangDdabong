from writers.models import PointLog

TODAY_MESSAGES = [
    "오늘은 어떤 고민을 전달해볼까요?",
    "하하하",
    "히히히",
]

Yang = {
    "new_yang": {
        "name": "신규 유저",
        "price": 0,
        "image": "",
        "description": "",
    },
    "young_yang": {
        "name": "어린양",
        "price": 5,
        "image": "",
        "description": "하루 당 +1 고민",
    },
    "very_yang": {
        "name": "버리양",
        "price": 20,
        "image": "",
        "description": "하루 당 +3 고민",
    },
    "worry_yang": {
        "name": "워리양",
        "price": 50,
        "image": "",
        "description": "하루 당 +1 고민\n새벽 배송 입장 가능",
    },
}

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
