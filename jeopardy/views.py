from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Topic, Question, BonusQuestion, Points
from django.core.urlresolvers import reverse
from random import randint

def index(request):
    request.session['jeopardy_game'] = {}
    request.session['jeopardy_questions'] = []
    games = Game.objects.all()
    return render(request, "jeopardy/index.html", {
        "games": games,
    })

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        if 'thumbs_up' in request.POST or 'thumbs_down' in request.POST:
            question = BonusQuestion.objects.get(pk=request.POST['question'])
            if 'thumbs_up' in request.POST:
                return render(request, "jeopardy/points.html", {
                    "game": game,
                    "question": question,
                    "bonus": True,
                    "players": request.session['jeopardy_game'].items(),
                })
            else:
                return redirect(reverse("jeopardy-scores"))
        else:
            request.session['jeopardy_game'] = {name: 0 for name in request.POST.getlist('name') if name}
            request.session['jeopardy_questions'] = []
    elif not request.session.get('jeopardy_game'):
        return render(request, "jeopardy/signup.html", {
            "numbers": list(range(5)),
        })
    questions = Question.objects.filter(game=game)
    topics = Topic.objects.filter(game=game)
    points = Points.objects.filter(game=game)
    if len(request.session['jeopardy_questions']) == len(topics) * len(points):
        questions = BonusQuestion.objects.filter(game=game.pk)
        question = questions[randint(0, questions.count() - 1)]
        return render(request, "jeopardy/question.html", {
            "game": game,
            "question": question,
            "bonus": True,
        })
    return render(request, "jeopardy/game.html", {
        "game": game,
        "questions": questions,
        "topics": topics,
        "points": points,
        "questions_done": request.session['jeopardy_questions'],
        "players": request.session['jeopardy_game'].items(),
    })

def give_points(request, game_id, question_id):
    if request.method == "POST":
        player = request.POST.get('player')
        if "bonus" in request.POST:
            question = BonusQuestion.objects.get(pk=question_id)
            request.session['jeopardy_game'][player] += question.value
            request.session.modified = True
            return redirect(reverse("jeopardy-scores"))
        else:
            question = Question.objects.get(pk=question_id)
            request.session['jeopardy_game'][player] += question.points.value + question.bonus
            request.session.modified = True
    return redirect(reverse("jeopardy-game", kwargs={"game_id": game_id}))

def scores(request):
    return render(request, "jeopardy/scores.html", {
        "players": request.session['jeopardy_game'].items(),
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
        "bonus": False,
    })
