from django.conf.urls import include, url
from .views import index, game, question

urlpatterns = [
    url(r'^$', index, name='jeopardy'),
    url(r'^game/(?P<game_id>\d*)/$', game, name="jeopardy-game"),
    url(r'^question/(?P<game_id>\d*)/(?P<topic_id>\d*)/(?P<point_id>\d*)/$', question, name="jeopardy-question"),
]
