from django.urls import path
from .views import WordDefinition

urlpatterns = [
    path('<str:word>/', WordDefinition.as_view()),
]