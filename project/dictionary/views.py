from django.shortcuts import render

# Create your views here.
# dictionary/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer
import requests

# dictionary/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class WordDefinition(APIView):
    def get(self, request, word):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response = requests.get(url)
        if response.status_code == 200:
            definitions = response.json()
            return Response(definitions)
        else:
            return Response({"error": "Word not found"}, status=response.status_code)

