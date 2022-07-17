from django.conf.urls import url
from django.urls import path

from .views import get_all_question, answer_search, article_search, get_all_article

urlpatterns = [
    url('questions/', get_all_question, name='all_ques'),
    url('articles/', get_all_article, name='all_article'),
    path('answer/<int:qid>/', answer_search, name='answer'),
    path('article/<int:aid>/', article_search, name='article'),
]
