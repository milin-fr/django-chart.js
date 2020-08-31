from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms.models import model_to_dict

from .models import Question, Choice


# Get questions and display them
def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)


# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })


# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Provide vote results in json format
def get_votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = []
    for choice in question.choice_set.all():
        choices.append(model_to_dict(choice))
    return JsonResponse(choices, safe=False)


# Display chart page
def chart(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/chart.html', { 'question': question })