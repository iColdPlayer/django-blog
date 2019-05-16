from django.shortcuts import render

def HomeIndex(request):
    return render(request, 'home.html')