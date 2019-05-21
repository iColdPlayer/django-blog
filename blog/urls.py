from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from .views import PostList, PostCreate


urlpatterns = [
    path('', PostList.as_view(), name='BlogIndex'),
    path('create/', PostCreate.as_view(), name='CreatePost'),
    path('<slug:slug>/', views.PostDetail, name='PostDetail'),

]