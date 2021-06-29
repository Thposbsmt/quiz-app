from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=5)