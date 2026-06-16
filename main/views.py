from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def worrywrite(request):
    if request.method == "POST":
        return redirect("home")

    return render(request, "worrywrite.html")