from accounts.models import Profile


def user_status(request):
    if not request.user.is_authenticated:
        return {}

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return {}

    return {
        "profile": profile,
        "worry_count": profile.worry_count,
        "points": profile.points,
    }
