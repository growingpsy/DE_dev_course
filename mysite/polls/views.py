from django.http import HttpResponse
from .models import *
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': latest_question_list}
    #context = {'questions': []}
    return render(request, 'polls/index.html', context)

def some_url(request):
    return HttpResponse("Some_url 구현하기")

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})