from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-publish_date')
    
    context = OrderedDict(
        question_list = question_list
    )

    return HttpResponse(render(request, "polls/index.html", context))

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    context = OrderedDict(
        question = question
    )

    return render(request, "polls/detail.html", context)

def results(request, question_id):
    return HttpResponse("You're looking at the results of question {}.".format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))



