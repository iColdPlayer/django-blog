from django.shortcuts import render
from blog.models import Post

def BlogIndex(request):
    posts = Post.objects.all().order_by("-created")
    context = {"posts":posts}
    return render(request, 'blog.html', context)


def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post": post,
    }
    return render(request, 'post.html', context)