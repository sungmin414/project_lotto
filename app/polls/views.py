from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context )


def results(request, question_id):
    response = "Question id: %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vote Page: %s" % question_id)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
