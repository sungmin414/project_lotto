from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
# 오브젝트를 생성하는 뷰 , 폼하고 모델하고 연결해서 새로운 데이터를 넣을때 사용
from django.views.generic.edit import CreateView
# 아이디,패스워드만 확인, 이메일은 없어서 따로 추가
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UploadForm


# login_required 로그인한사람만 업로드할수있게 해줌
@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')
    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form': form})


class IndexView(ListView):
    # model = Photo
    context_object_name = 'user_photo_list'
    # 사진 2개씩 나오게하기
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')

#
# class CreateUserView(CreateView):
#     template_name = 'registration/signup.html'
#     form_class = CreateUserForm
#     # form_class = UserCreationForm
#     # reverse_lazy 재내릭뷰같은경우 로딩하는 문제때문에
#     success_url = reverse_lazy('create_user_done')
#
#
# class RegisteredView(TemplateView):
#     template_name = 'registration/signup_done.html'


class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'kilogram/profile.html'
