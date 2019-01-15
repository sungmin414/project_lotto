from django.conf import settings
from django.db import models

# Create your models here.\
from django.shortcuts import get_object_or_404, render
from django.views import View

from .forms import UserForm, ProfileForm


def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    # honux/absdfer.png
    return '%s/%s.%s' % (instance.owner.username, pid, extension)


class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    thumnail_image = models.ImageField(blank=True)
    comment  = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=True)
    profile_photo = models.ImageField(blank=True)
    nickname = models.CharField(max_length=64)


class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk = request.user.pk)
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
            profile_file = ProfileForm()

        return render(request, 'kilogram/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})


        
