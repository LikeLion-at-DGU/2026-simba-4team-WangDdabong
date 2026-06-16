from django.shortcuts import render

# Create your views here.

def demo_home(request):
    return render(request, 'main/demo_home.html')