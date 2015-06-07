from django.conf.urls import include, url
from .views import index, game, question, play

urlpatterns = [
    url(r'^$', index, name='million'),
    url(r'^game/(?P<game_id>\d*)/$', game, name="million-game"),
    url(r'^game/(?P<game_id>\d*)/play/$', play, name="million-play"),
    url(r'^question/(?P<question_id>\d*)/$', question, name="million-question"),
]