from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import article

# Create your views here.

def index(request):
    return render_to_response('news/index.html')

def index2(request):
    return render_to_response('news/index_template.html')


def article(request, id):
#    post = get_object_or_404()
#    return render(request, 'news/detail.html', {'post':post})
    return render_to_response('news/article.html')

def article2(request, id):
    return render_to_response('news/article_template.html', {'article':article})