from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='top'),
    url(r'^top$', views.index2, name='top'),
#    url(r'^article/$', views.article, name='article'),
    url(r'^article/(?P<id>\d+)$', views.article, name='articles'),
    url(r'^example/(?P<id>\d+)$', views.article2, name='articles'),
]