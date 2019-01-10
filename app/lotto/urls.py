from django.urls import path
from . import views

app_name = 'lotto'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.post, name='new_lotto'),
    path('<int:lottokey>/detail/', views.detail, name='detail'),
]