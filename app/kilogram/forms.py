from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Photo, Profile


# class CreateUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     def save(self, commit=True):
#         user = super(CreateUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class UploadForm(forms.ModelForm):
    comment = forms.CharField(max_length=255)

    class Meta:
        model = Photo
        exclude = ('thumnail_image', 'owner')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_photo']


