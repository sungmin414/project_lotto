from django.conf import settings
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.\
from django.shortcuts import get_object_or_404, render
from django.views import View


# instance(photo), filename(업로된 파일이름)가르킴
def user_path(instance, filename):
    from random import choice
    import string

    # 무작위 8글자를 뽑아줌
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    # 파일확장자
    extension = filename.split('.')[-1]
    # honux/absdfer.png
    return '%s/%s.%s' % (instance.owner.username, pid, extension)


class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    # thumnail_image = models.ImageField(blank=True)
    comment  = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return '{}{}{}'.format(self.owner.username, self.comment, self.is_public)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=True)
    profile_photo = models.ImageField(blank=True)
    nickname = models.CharField(max_length=64)


