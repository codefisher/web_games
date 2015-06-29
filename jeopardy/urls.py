from django.conf.urls import url
from .views import index, game, question, give_points, scores, bonus

urlpatterns = [
    url(r'^$', index, name='jeopardy'),
    url(r'^game/(?P<game_id>\d+)/$', game, name="jeopardy-game"),
    url(r'^bonus/(?P<game_id>\d+)/$', bonus, name="jeopardy-bonus"),
    url(r'^scores/(?P<game_id>\d+)/$', scores, name="jeopardy-scores"),
    url(r'^points/(?P<game_id>\d+)/(?P<question_id>\d+)/$', give_points, name="jeopardy-game-points"),
    url(r'^question/(?P<game_id>\d+)/(?P<topic_id>\d+)/(?P<point_id>\d+)/$', question, name="jeopardy-question"),
]
