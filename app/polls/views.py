from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello, CodeSquad')


def results(request, question_id):
    response = "Question id: %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vote Page: %s" % question_id)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
