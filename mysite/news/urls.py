from django.conf.urls import url
from . import views
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='top'),
    url(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='articles'),
]
