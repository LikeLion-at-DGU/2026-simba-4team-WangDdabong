from django.contrib.auth.models import User
from django.shortcuts import render , get_object_or_404
from accounts.models import Profile

# Create your views here.

def mypage(request, id):
    profile_writer = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, writer=profile_writer)

    context = {
        'profile_writer' : profile_writer,
        'profile' : profile,
    }

    return render(request, 'writers/mypage.html', context)