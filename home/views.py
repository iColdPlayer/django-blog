from django.shortcuts import render
from blog.models import Post


def HomeIndex(request):
    posts = Post.objects.all().order_by('-created')[0:3]
    context =  {"posts": posts}
    return render(request, 'home.html', context)


def error404(request, exception):
    return render(request,'404.html')