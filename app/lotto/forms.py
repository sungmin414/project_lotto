from django import forms
from .models import GuessNumbers


class PostForm(forms.ModelForm):

    class Meta:
        # 사용할 model
        model = GuessNumbers
        # 입력받을 필드
        fields = ('name', 'text',)