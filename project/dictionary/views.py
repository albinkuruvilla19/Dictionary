from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import generics
from .models import WordOfTheDay
from .serializers import WordOfTheDaySerializer



class word_list(generics.ListCreateAPIView):
    serializer_class = WordOfTheDaySerializer

    def get_queryset(self):
        queryset = WordOfTheDay.objects.all()
        return queryset
    
class word_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WordOfTheDaySerializer
    queryset = WordOfTheDay.objects.all()


class WordDefinition(APIView):
    def get(self, request, word):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response = requests.get(url)
        if response.status_code == 200:
            definitions = response.json()
            return Response(definitions)
        else:
            return Response({"error": "Word not found"}, status=response.status_code)