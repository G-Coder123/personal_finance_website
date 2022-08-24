from django.db import models
from django.urls import reverse

class Quiz(models.Model):
    title= models.CharField(max_length=255)
    topic= models.CharField(max_length=255)
    answer1= models.CharField(max_length=255)
    answer2= models.CharField(max_length=255)
    answer3=models.CharField(max_length=255)
    correctAnswer=models.CharField(default="Nothing", max_length=255)
    def __str__(self):
        return f"{self.title} | {self.answer1}| {self.topic}| {self.answer2}| {self.answer3}| {self.correctAnswer}"