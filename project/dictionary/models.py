from django.db import models

# Create your models here.
# dictionary/models.py

from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word
