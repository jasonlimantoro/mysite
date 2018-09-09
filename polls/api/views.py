from django.http import JsonResponse
from ..models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5].values()
    return JsonResponse(list(questions), safe=False)

def show(request, question_id):
    question = Question.objects.filter(pk=question_id).values()
    return JsonResponse(list(question)[0], safe=False)
