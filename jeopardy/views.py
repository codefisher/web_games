import json
import os
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Topic, Question, BonusQuestion, Points, Result, Player
from django.urls import reverse
from operator import itemgetter
from random import randint
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import formset_factory
from django.conf import settings

def index(request):
    request.session['jeopardy_game'] = []
    request.session['jeopardy_questions'] = []
    request.session['jeopardy_sounds'] = {}
    games = Game.objects.filter(hidden=False)
    return render(request, "jeopardy/index.html", {
        "games": games,
    })

def bonus(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        question = BonusQuestion.objects.get(pk=request.POST['question'])
        if 'thumbs_up' in request.POST:
            template = "jeopardy/points.html"
        else:
            template = "jeopardy/wrong.html"
        player_input = request.POST.get('player')
        if player_input and player_input.isdigit():
            player = int(player_input) + 1
        else:
            player = None
        return render(request, template, {
            "game": game,
            "question": question,
            "bonus": True,
            "player_number": player,
            "players": request.session['jeopardy_game'],
        })
    questions = BonusQuestion.objects.filter(game=game.pk)
    question = questions[randint(0, questions.count() - 1)]
    return render(request, "jeopardy/question.html", {
        "game": game,
        "question": question,
        "bonus": True,
        "players": request.session['jeopardy_game'],
        "names": json.dumps([name for name, points in request.session['jeopardy_game']]),
        "sounds": json.dumps(request.session['jeopardy_sounds'])
    })

class PlayerForm(forms.Form):
     name = forms.CharField(label=_('Name'))
     sound = forms.FileField(required=False, label=_('Sound'))
PlayerFormSet = formset_factory(PlayerForm, extra=5)

def handle_uploaded_file(f):
    if not f:
        return ''
    with open(os.path.join(settings.MEDIA_ROOT, 'jeopardy', f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return settings.MEDIA_URL + "jeopardy/" + f.name

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        formset = PlayerFormSet(request.POST, request.FILES)
        if formset.is_valid():
            request.session['jeopardy_game'] = [[row['name'], 0] for row in formset.cleaned_data if row.get('name')]
            request.session['jeopardy_sounds'] = {row['name']: handle_uploaded_file(row['sound']) for row in formset.cleaned_data if row.get('sound')}
            request.session['jeopardy_questions'] = []
    elif not request.session.get('jeopardy_game'):
        return render(request, "jeopardy/signup.html", {
            "players": PlayerFormSet,
        })
    questions = Question.objects.filter(game=game)
    topics = Topic.objects.filter(game=game)
    points = Points.objects.filter(game=game)
    remaining = ((len(topics) * len(points)) - len(request.session['jeopardy_questions']))
    show_bonus = (len(request.session['jeopardy_questions']) == len(topics) * len(points))
    return render(request, "jeopardy/game.html", {
        "game": game,
        "questions": questions,
        "topics": topics,
        "points": points,
        "remaining": remaining,
        "show_bonus": show_bonus,
        "questions_done": request.session['jeopardy_questions'],
        "players": request.session['jeopardy_game'],
    })

def add_points(data, player, value):
    for i, (name, points) in enumerate(data):
        if player == name:
            data[i][1] += value
            break

def give_points(request, game_id, question_id):
    if request.method == "POST":
        if 'player' not in request.POST:
            return redirect(reverse("jeopardy-game", kwargs={"game_id": game_id}))
        player = request.POST.get('player')
        if "bonus" in request.POST:
            question = BonusQuestion.objects.get(pk=question_id)
            add_points(request.session['jeopardy_game'], player, question.value)
            request.session.modified = True
            return redirect(reverse("jeopardy-scores", kwargs={"game_id": game_id}))
        else:
            question = Question.objects.get(pk=question_id)
            add_points(request.session['jeopardy_game'], player, question.points.value + question.bonus)
            request.session.modified = True
    return redirect(reverse("jeopardy-game", kwargs={"game_id": game_id}))

def scores(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    players = list(reversed(sorted(
        request.session['jeopardy_game'], key=itemgetter(1))))
    result = Result.objects.create(game=game)
    for player, points in players:
        player = Player.objects.create(result=result, name=player, points=points)
    return render(request, "jeopardy/scores.html", {
        "players": players,
        "game": game
    })

def question(request, game_id, topic_id, point_id):
    game = get_object_or_404(Game, pk=game_id)
    try:
        topic = Topic.objects.get(pk=topic_id)
        point = Points.objects.get(pk=point_id)
        question = Question.objects.get(game=game_id, topic=topic_id, points=point_id)
    except:
        return render(request, "jeopardy/no_question.html")
    if request.method == "POST":
        request.session['jeopardy_questions'].append((int(topic_id), int(point_id)))
        request.session.modified = True
        if 'thumbs_up' in request.POST:
            template = "jeopardy/points.html"
        else:
            template = "jeopardy/wrong.html"
        player_input = request.POST.get('player')
        if player_input and player_input.isdigit():
            player = int(player_input) + 1
        else:
            player = None
        return render(request, template, {
            "game": game,
            "topic": topic,
            "point": point,
            "question": question,
            "player_number": player,
            "players": request.session['jeopardy_game'],
        })
    return render(request, "jeopardy/question.html", {
        "game": game,
        "topic": topic,
        "point": point,
        "question": question,
        "bonus": False,
        "players": request.session['jeopardy_game'],
        "names": json.dumps([name for name, points in request.session['jeopardy_game']]),
        "sounds": json.dumps(request.session['jeopardy_sounds'])
    })
