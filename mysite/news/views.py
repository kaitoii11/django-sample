from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render_to_response
from django.http import Http404
from .models import Article

# Create your views here.
def index(request):
    return render_to_response('news/index.html')

class ArticleListView(ListView):
    model = Article

    def index2(request):
        return render_to_response('news/index_template.html')


def article(request, id):
#    post = get_object_or_404()
#    return render(request, 'news/detail.html', {'post':post})
    return render_to_response('news/article.html')

class ArticleDetailView(DetailView):
    model = Article
    def article2(request, id):
        try:
            a = article.objects.get(pk=id)
        except:
            raise Http404("Article does not exist")
        return render_to_response('news/article_template.html', {'article':a})
