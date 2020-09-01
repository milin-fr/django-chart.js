from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms.models import model_to_dict
import random

from .models import Question, Choice, Gamer


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


# Add a set of gamer entries to DB
def generate_gamers_in_db(request):

    return JsonResponse({"warning":"this command will generate 50k entries in db. If you want to execute it, update polls -> views -> generate_gamers_in_db"}, safe=False)

    avatar_name_suffix = avatar_name_core = avatar_name_prefix = ["Slayer", "Doom", "Mighty", "Magic", "Elf", "Dwarf", "Eagle", "Sword", "Gun", "Blast", "Fire", "Lord", "Warior", "Mage", "Rogue", "War", "Battle", "Champion", "Team", "Chosen"]
    for i in range(10000): # play few pay few
      gamer = Gamer()
      gamer.avatar_name = avatar_name_suffix[random.randint(0,19)] + avatar_name_core[random.randint(0,19)] + avatar_name_prefix[random.randint(0,19)]
      gamer.playtime = random.randint(1,100)
      gamer.money_spent = random.randint(1,10)
      gamer.save()

    for i in range(20000): # play lot pay few
      gamer = Gamer()
      gamer.avatar_name = avatar_name_suffix[random.randint(0,19)] + avatar_name_core[random.randint(0,19)] + avatar_name_prefix[random.randint(0,19)]
      gamer.playtime = random.randint(100,1000)
      gamer.money_spent = random.randint(1,10)
      gamer.save()
    
    for i in range(12000): # play lot pay lot
      gamer = Gamer()
      gamer.avatar_name = avatar_name_suffix[random.randint(0,19)] + avatar_name_core[random.randint(0,19)] + avatar_name_prefix[random.randint(0,19)]
      gamer.playtime = random.randint(100,1000)
      gamer.money_spent = random.randint(10,100)
      gamer.save()

    for i in range(8000): # play few pay lot
      gamer = Gamer()
      gamer.avatar_name = avatar_name_suffix[random.randint(0,19)] + avatar_name_core[random.randint(0,19)] + avatar_name_prefix[random.randint(0,19)]
      gamer.playtime = random.randint(1,100)
      gamer.money_spent = random.randint(10,100)
      gamer.save()

    # return JsonResponse({"resonse":"ok"}, safe=False)


# Display chart page for all gamers
def raw_gamer_chart(request):
    gamers = Gamer.objects.all()
    return render(request, 'polls/chart.html', { 'question': question })


# Get JSON data of all gamers
def get_gamers_json(request):
    gamers_data = []
    for gamer in Gamer.objects.all():
        gamers_data.append(model_to_dict(gamer))
    return JsonResponse(gamers_data, safe=False)