from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

def show(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/show.html', context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
