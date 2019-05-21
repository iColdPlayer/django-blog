from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, TemplateView
from blog.models import Post, UserPost
from blog import models


# class PostList(ListView):
#     model = Post
#     template_name = 'blog.html'
#     context_object_name = 'posts'
#     ordering =  ['created']



class PostList(ListView):
    template_name = 'blog.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Post.objects.all().order_by('-created')

    def get_context_data(self, **kwargs):
        PostIndex = super(PostList, self).get_context_data(**kwargs)
        PostIndex['posts'] = Post.objects.all().order_by('-created')
        PostIndex['userposts'] = UserPost.objects.all().order_by('-created')
        return PostIndex


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
    fields = ['title', 'slug', 'description', 'content', 'created']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)