from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
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
    request.session['game'] = game.pk
    request.session['question'] = 0
    return render(request, "million/game.html", {
        "game": game,
        "questions": questions,
    })

def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    questions = Question.objects.filter(game=game).order_by("value")
    if request.session.get('game') != game.pk:
        request.session['game'] = game.pk
        request.session['question'] = 0
        return redirect(reverse("million-question", kwargs={"question_id": questions[request.session.get('question')].pk}))
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=request.POST.get('question'))
        answer = request.POST.get('answer')
        correct = ((answer == 'one' and question.answer_one_correct)
            or (answer == 'two' and question.answer_two_correct)
            or (answer == 'three' and question.answer_three_correct)
            or (answer == 'four' and question.answer_four_correct))
        if correct:
            request.session['question'] += 1
        else:
            request.session['question'] = 0
        if request.session['question'] >= len(questions):
            return render(request, "million/million.html", {})
        return render(request, "million/result.html", {
            "game": game,
            "questions": questions,
            "correct": correct,
            "current": request.session['question'],
        })
    try:
        return redirect(reverse("million-question", kwargs={"question_id": questions[request.session.get('question')].pk}))
    except IndexError:
        return redirect(reverse("million-game", kwargs={"game_id": game.pk}))

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    questions = Question.objects.filter(game=question.game).order_by("value")
    return render(request, "million/question.html", {
        "game": question.game,
        "question": question,
        "questions": questions,
        "current": request.session['question'],
    })