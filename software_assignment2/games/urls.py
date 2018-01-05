from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^genres/$', views.genres, name='index'),
    url(r'^games/$', views.games, name='index'),
    url(r'^developers/$', views.developers, name='index'),
    url(r'^genres/(?P<genres_id>[0-9]+)/$', views.detail1, name='detail1'),
    url(r'^genres/games/(?P<games_id>[0-9]+)/$', views.detail2, name='detail2'),
    url(r'^genres/games/developers/(?P<developers_id>[0-9]+)/$', views.detail3, name='detail3'),
]
