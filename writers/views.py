from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from worries.models import Worry
from .models import *

# Create your views here.

def mypage(request, id):
    profile_writer = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, writer=profile_writer)

    context = {
        'profile_writer' : profile_writer,
        'profile' : profile,
    }

    return render(request, 'writers/mypage.html', context)

def post_epilogue(request, worry_id):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    worry = get_object_or_404(Worry, pk=worry_id)
    worry.is_HoF = request.POST["is_HoF"]

    new_epilogue = Epilogue()

    new_epilogue.worry = worry
    new_epilogue.writer = request.user
    new_epilogue.ep_han_madi = request.POST["ep_han_madi"]
    new_epilogue.ep_title = request.POST["ep_title"]
    new_epilogue.ep_content = request.POST["ep_content"]

    new_epilogue.save()

    return redirect("main:demo_home", {"source": "post_epilogue"})