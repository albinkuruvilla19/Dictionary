from django.urls import path
from .views import WordDefinition,word_detail,word_list

urlpatterns = [
    path('<str:word>/', WordDefinition.as_view()),
    path('list/words/', word_list.as_view()),
    path('list/words/<int:pk>/', word_detail.as_view()),
]

