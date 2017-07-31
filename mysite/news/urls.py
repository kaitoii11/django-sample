from django.conf.urls import url
from . import views
from views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', views.index, name='top'),
    url(r'^top$', ArticleListView.as_view(), name='top'),
    url(r'^article/(?P<id>\d+)$', views.article, name='articles'),
    url(r'^example/(?P<id>\d+)$', views.ArticleDetailView.as_view(), name='articles2'),
]
