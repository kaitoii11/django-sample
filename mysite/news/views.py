from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render_to_response
from django.http import Http404
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    template_name='news/index_template.html'
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'news/article_template.html'
    model = Article
