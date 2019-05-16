from django.urls import path
from blog import views

urlpatterns = [
    path('', views.BlogIndex, name='BlogIndex'),
    path('<slug:slug>/', views.PostDetail, name='PostDetail')
]