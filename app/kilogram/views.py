from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView, View
# 오브젝트를 생성하는 뷰 , 폼하고 모델하고 연결해서 새로운 데이터를 넣을때 사용
from django.views.generic.edit import CreateView
# 아이디,패스워드만 확인, 이메일은 없어서 따로 추가
from django.contrib.auth.forms import UserCreationForm
from .forms import UploadForm, UserForm, ProfileForm


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


class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)

        user_form = UserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname': profile.nickname,
                'profile_photo': profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'kilogram/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request):
        pk = request.user.pk
        u = User.objects.get(id=request.user.pk)
        user_form = UserForm(request.POST, instance=u)

        if (user_form.is_valid()):
            user_form.save()

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = u
            profile.save()

        return redirect('kilogram:profile', pk)