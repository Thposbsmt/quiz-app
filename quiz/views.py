from django.shortcuts import render, loader
from django.http import HttpResponse
import random

from .models import Quiz

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