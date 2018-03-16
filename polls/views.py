from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime 

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class LoanFormView(generic.ListView):
    model = Question
    template_name = 'polls/loanform.html'
class DecisionView(generic.ListView):
    model = Question
    template_name = 'polls/decision.html'
#class NoView(generic.DetailView):
 #   model = X
  #  template_name = 'polls'


#def vote(request, question_id):
    ... # same as above, no changes needed.



def index(request):
    if question.pub_date()<=timezone.now():
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    else:
        latest_question_list = []
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request):
	try:
		question = get_object_or_404(Question, pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
		return render(request, 'polls/detail.html', {'question': question})
def loanform(request):
    if question.pub_date()<=timezone.now():
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    else:
        latest_question_list = []
    template = loader.get_template('polls/loanform.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def decision(request):
    if question.pub_date()<=timezone.now():
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    else:
        latest_question_list = []
    template = loader.get_template('polls/decision.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    

    #try:
        #question = get_object_or_404(Question)
    #def detail(request, question_id):
    #try:
        #question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
      #  raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)
def results(request):
    question = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/results.html', {'question':question})
	

def vote(request, question_id):
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