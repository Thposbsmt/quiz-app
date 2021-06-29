from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    correct_answer = models.CharField(max_length=5)
    
    def __str__(self):
        return self.question