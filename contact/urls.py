from django.urls import path
from contact import views

urlpatterns = [
    path('', views.About, name='About' )
]