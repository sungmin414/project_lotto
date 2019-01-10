from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
# 오브젝트를 생성하는 뷰 , 폼하고 모델하고 연결해서 새로운 데이터를 넣을때 사용
from django.views.generic.edit import CreateView
# 아이디,패스워드만 확인, 이메일은 없어서 따로 추가
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


class IndexView(TemplateView):
    template_name = 'kilogram/index.html'


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    # form_class = UserCreationForm
    # reverse_lazy 재내릭뷰같은경우 로딩하는 문제때문에
    success_url = reverse_lazy('create_user_done')


class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
