from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context )


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question":question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id = question_id)


def detail(request, question_id):
    # try:
        # q = Question.objects.get(pk = question_id)
        q = get_object_or_404(Question, pk = question_id)
        context = {'question': q}
    # except Question.DoesNotExist:
    #     raise Http404('Question %s does not exist' % question_id)
        return render(request, 'polls/detail.html', context)
