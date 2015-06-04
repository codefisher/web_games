from django.shortcuts import render, get_object_or_404
from .models import Game, Question
# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request, "million/index.html", {
        "games": games,
    })

def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    questions = Question.objects.filter(game=game).order_by("value")
    return render(request, "million/game.html", {
        "game": game,
        "questions": questions,
    })

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "million/question.html", {
        "question": question,
    })