# 인증 - 로그인 구현하기

## css 추가 

지난 시간에 빠진 css 파일을 추가합니다.

- kilogram/static/kilogram/style.css

```
a {
    color: green;
    text-decoration: none;
}
``` 

base.html 템플릿에는 `{% load static %}` 구문이 있는데 `{% load staticfiles %}` 로 고칠 수 있습니다. 
이 경우 `python manage.py collectstatic` 명령을 서버 실행 전에 수행해야 합니다. 
(관련 링크: http://stackoverflow.com/questions/24238496/what-is-the-difference-between-load-staticfiles-and-load-static)

## 로그인용 사용자 생성해 보기

```
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('chiken1', 'chiken1@out.org', 'pass5678')
```

완료 후 admin 툴을 이용해서 확인해 봅시다. 

## model

장고의 django.contrib.auth.models.User 를 그대로 사용합니다.
특별한 코딩은 필요하지 않습니다.

## auth 관련 url 추가하기

장고에 기본으로 내장된 인증 기능을 활용합니다. 

- settings/urls.py 수정 

```
urlpatterns = [
  url(r'^accounts/', include('django.contrib.auth.urls')),
]
```

auth.urls를 include 할 경우 아래와 같은 url들이 포함됩니다.

```
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
```

## view 만들기

login 관련 기능에는 별도로 view를 작성할 필요 없이 템플릿만 작성하면 됩니다. 

## template 만들기

로그인과 로그아웃에 사용할 템플릿을 만듭니다. 경로와 이름이 이미 정해져 있는데 로그인은 만들지 않으면 에러가 발생하고, 로그 아웃은 관리자용 페이지를 사용합니다. 
둘 다 모두 직접 만들어 주는 것이 좋습니다. 

- base.html 수정

로그인 및 로그아웃 링크를 추가합니다. 로그인한 상태와 로그인하지 않은 상태에서 보여줄 링크도 변경합니다.

```html
<ul class="nav navbar-nav navbar-right">
  {% if user.is_active %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-heart"></span> {{user.username}}</a></li>
  <li><a href="{% url 'logout' %}">Logout</a></li>
  {% else %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-user"></span> Login</a></li>
  <li><a href="{% url 'admin:index' %}">Admin</a></li>
  {% endif %}
</ul>
```

- registration/login.html

```
{% extends 'kilogram/base.html' %}
{% block content %}

{% if user.is_active %}
<h2> Welcome, {{user.username}} </h2>
<a href="{% url 'logout' %}">로그아웃</a>

{% else %}
{% if form.errors %}
<p>ID나 비밀번호가 일치하지 않습니다.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}
<input type="hidden" name="next" value="" />
{{ form.as_p }}
<button type="submit">로그인</button>
</form>

{% endif %}

{% endblock %}
```

## settings.py 수정

로그인후 리다이렉트 페이지는 기본적으로 /accounts/profile 로 지정되어 있는데 이를 변경합니다.
settings.py의 가장 아래에 아래 내용을 추가합니다.

```
# Auth settings
LOGIN_REDIRECT_URL = '/kilogram/'
```

## 로그아웃용 template 만들기

- registration/logged_out.html

로그아웃용 파일입니다. 템플릿 이름이 다르면 안 됩니다. 파일이름은 장고 소스의 auth.views.logout()을 보시면 확인할 수 있습니다.

```
{% extends 'kilogram/base.html' %}
{% block content %}

<h2> 잘 가요, 안녕. </h2>
<p><a href="{%url 'login'%}">다시 로그인하기</a></p>

{% endblock %}

```

## 참고 링크. 
- https://docs.djangoproject.com/en/1.10/ref/urlresolvers/
- https://docs.djangoproject.com/en/1.10/topics/auth/default/