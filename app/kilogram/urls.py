from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'kilogram'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('upload/', views.upload, name='upload'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile_update/', login_required(views.ProfileUpdateView.as_view()), name='profile_update'),

]