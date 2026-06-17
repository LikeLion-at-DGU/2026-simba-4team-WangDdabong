from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def worry_write(request):
    if request.method == "POST":
        return redirect("home")

    return render(request, "worry_write.html")

def worry_list(request):
    return render(request, "worry_list.html")

def worry_detail(request):
    return render(request, "worry_detail.html")

def worry_reply(request):
    return render(request, "worry_reply.html")