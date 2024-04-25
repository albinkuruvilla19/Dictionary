# serializers.py
from rest_framework import serializers
from .models import WordOfTheDay

class WordOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WordOfTheDay
        fields = ['id', 'word', 'definition', 'date']
