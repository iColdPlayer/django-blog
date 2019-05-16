from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('register/', views.Register, name='Register')
]
