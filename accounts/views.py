from django.shortcuts import render

def Login(request):
    return render(request, 'login.html' )

def Register(request):
    return render(request, 'register.html')