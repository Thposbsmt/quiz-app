from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView
import random

from .models import Quiz
from .forms import QuizForm, BooleanForm    

def index(request):
    template = loader.get_template('quiz/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def test(request):
    if request.method == 'POST':
        form1 = BooleanForm(request.POST, prefix="1")
        form2 = BooleanForm(request.POST, prefix="2")
        form3 = BooleanForm(request.POST, prefix="3")
        
        answer1 = request.POST['hidden_answer0']
        answer2 = request.POST['hidden_answer1']
        answer3 = request.POST['hidden_answer2']
        print(answer1)
        print(answer2)
        print(answer3)
        counter = 0
        
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            if form1.cleaned_data['choice'] == answer1:
                counter += 1
            if form2.cleaned_data['choice'] == answer2:
                counter += 1
            if form3.cleaned_data['choice'] == answer3:
                counter += 1
            return render(request, "quiz/result.html", {"counter":counter})
    else:
        items = list(Quiz.objects.all())
        random_items = random.sample(items, 3)
        form1 = BooleanForm(prefix="1")
        form2 = BooleanForm(prefix="2")
        form3 = BooleanForm(prefix="3")
        context = {'quizes':random_items, 'form1':form1, 'form2':form2, 'form3':form3}
        
        return render(request, "quiz/test.html", context)
    

class QuizCreateView(CreateView):
    template_name = 'quiz/create.html'
    form_class = QuizForm
    success_url = '/'