from django.urls import path
from . import views

urlpatterns = [
    path('lotto/', views.index, name='lotto'),
    path('', views.index, name='index'),
    path('lotto/new/', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail/', views.detail, name='detail'),
]