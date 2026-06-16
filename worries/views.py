from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def write_worry(request):
    # if not request.user.is_authenticated:
    #     return redirect("accounts:login")
    
    new_worry = Worry()

    new_worry.writer = request.user
    new_worry.keyword = request.POST["keyword"]
    new_worry.title = request.POST["title"]
    new_worry.content = request.POST["content"]
    new_worry.mbti = request.POST["mbti"]

    new_worry.save()

    # return redirect("main:demo_firstpage")
    return render(request, "worries/demo_write_worry.html")