from django.conf.urls import include, url
from .views import index, game, question, play, retire

urlpatterns = [
    url(r'^$', index, name='million'),
    url(r'^game/(?P<game_id>\d*)/$', game, name="million-game"),
    url(r'^game/(?P<game_id>\d*)/play/$', play, name="million-play"),
    url(r'^game/(?P<game_id>\d*)/retire/$', retire, name="million-retire"),
    url(r'^question/(?P<question_id>\d*)/((?P<action>[a-z]*)/)?$', question, name="million-question"),
]
