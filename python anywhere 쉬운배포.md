## 내용정리


### pythonanywhere 회원가입
이메일만으로 쉽게 가입 가능

## bash 실행
```
$ git clone https://github.com/honux77/lotto-web
$ tree lotto-web
```

## virtualenv 설정
```
$ virtualenv --python=python3.5 lottoenv
$ source lottoenv/bin/activate
$ pip install django==1.10 whitenoise
```

## 서버 설정
```
$ cd lotto-web
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py createsuperuser
```

## web - virtualenv 설정
```
/home/<your-username>/lottoenv/
```


## web - WSGI 설정
```
import os
import sys

path = '/home/<your-username>/lotto-web'  # 여러분의 유저네임을 여기에 적어주세요.
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
```
## secret key 생성
```
$ python genkey.py
```
## settings.py 수정
```
DEBUG=False
ALLOWED_HOST=[honux.pythonanywhere.com]
SECRET_KEY= '....'
```

## 404오류 처리방법(2가지 다른방법도 더있음 문서 참조)

    
    def detail(request, question_id):
        # try:
            # q = Question.objects.get(pk = question_id)
            q = get_object_or_404(Question, pk = question_id)
            context = {'question': q}
        # except Question.DoesNotExist:
        #     raise Http404('Question %s does not exist' % question_id)
            return render(request, 'polls/detail.html', context)



