from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render_to_response('news/index.html')


# def article(request, pk):
#    post = get_object_or_404()
#    return render(request, 'news/detail.html', {'post':post})
def article(request):
    return render_to_response('news/article.html')
