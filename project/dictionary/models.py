from django.db import models

# Create your models here

class Word(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word


class WordOfTheDay(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    date = models.DateField(auto_now_add=True)
