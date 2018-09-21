from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# gk salah, tapi kalo gw pribadi, lebih suka function based view, soalnya kalo pake class based terlalu abstract
# takutnya ada bug/behavior di DetailView yg gw gk tau
class EditView(generic.DetailView):
    model = Question
    template_name = 'polls/edit.html'

class ShowView(generic.DetailView):
    model = Question
    template_name = 'polls/show.html'

def vote(request, question_id):
    # nah ini lu pake get_object_or_404, knp di tempat lain ngk
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/edit.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # ini biar aman, pake F() query, biar gk kena race condition
        # jadi: selected_choice.votes = F('votes') + 1
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:show', args=(question.id,)))
