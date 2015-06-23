from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Topic, Question, BonusQuestion, Points
from django.core.urlresolvers import reverse

def index(request):
    request.session['jeopardy_game'] = None
    request.session['jeopardy_questions'] = []
    games = Game.objects.all()
    return render(request, "jeopardy/index.html", {
        "games": games,
    })

def game(request, game_id):
    if request.method == "POST":
        request.session['jeopardy_game'] = {name: 0 for name in request.POST.getlist('name') if name}
        request.session['jeopardy_questions'] = []
    elif request.session.get('jeopardy_game') is None:
        return render(request, "jeopardy/signup.html", {
            "numbers": list(range(5)),
        })
    game = get_object_or_404(Game, pk=game_id)
    questions = Question.objects.filter(game=game)
    topics = Topic.objects.filter(game=game)
    points = Points.objects.filter(game=game)
    return render(request, "jeopardy/game.html", {
        "game": game,
        "questions": questions,
        "topics": topics,
        "points": points,
        "players": request.session.get('jeopardy_game', {}).items(),
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
        request.session['jeopardy_questions'].append((topic, point))
        if 'thumbs_up' in request.POST:
            return render(request, "jeopardy/points.html", {
                "game": game,
                "topic": topic,
                "point": point,
                "question": question,
                "players": request.session['jeopardy_game'].items(),
            })
        else:
            return redirect(reverse("jeopardy-game", kwargs={"game_id": game.pk}))
    return render(request, "jeopardy/question.html", {
        "game": game,
        "topic": topic,
        "point": point,
        "question": question,
    })
