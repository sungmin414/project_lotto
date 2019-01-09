from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

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
    # try:
        # q = Question.objects.get(pk = question_id)
        q = get_object_or_404(Question, pk = question_id)
        context = {'question': q}
    # except Question.DoesNotExist:
    #     raise Http404('Question %s does not exist' % question_id)
        return render(request, 'polls/detail.html', context)
