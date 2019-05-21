from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from blog.models import Post, UserPost



class PostList(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    ordering =  ['created']


# def BlogIndex(request):
#     posts = Post.objects.all().order_by("-created")
#     context = {"posts":posts}
#     return render(request, 'blog.html', context)


def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post": post,
    }
    return render(request, 'post.html', context)



class PostCreate(CreateView):
    model = UserPost
    fields = ['title', 'description', 'content', 'created']
    template_name = 'create.html'