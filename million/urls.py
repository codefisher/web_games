from django.conf.urls import include, url
from .views import index, game, question

urlpatterns = [
    url(r'^$', index),
    url(r'^game/(?P<game_id>\d*)/$', game, name="million-game"),
    url(r'^question/(?P<question_id>\d*)/$', question, name="million-question"),
]
