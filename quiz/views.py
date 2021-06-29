from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView
import random

from .models import Quiz
from .forms import QuizForm

def index(request):
    template = loader.get_template('quiz/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.get_template('quiz/test.html')
    
    items = list(Quiz.objects.all())
    random_items = random.sample(items, 3)
    
    context = {'quizes':random_items}
    
    return HttpResponse(template.render(context, request))

class QuizCreateView(CreateView):
    template_name = 'quiz/create.html'
    form_class = QuizForm
    success_url = '/'