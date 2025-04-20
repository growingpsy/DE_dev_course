from .models import *
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    #context = {'questions': []}
    return render(request, 'polls/index.html', context)

def some_url(request):
    return HttpResponse("Some_url 구현하기")

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Question, pk=question_id)  
    return render(request, 'polls/detail.html', {'question': question})