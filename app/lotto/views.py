from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm
from .models import GuessNumbers


def index(request):
    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})


def post(request):
    if request.method == 'POST':
        # save data
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('lotto')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})