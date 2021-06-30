from django.forms import ModelForm
from django import forms

BOOLEAN = [
    ("True",'True'),
    ("False","False"),
]

from .models import Quiz

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ('question', 'correct_answer')
        
class BooleanForm(forms.Form):
    choice = forms.ChoiceField(label='',choices=BOOLEAN, widget=forms.RadioSelect)