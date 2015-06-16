import random
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
    request.session['call'] = True
    request.session['audience'] = True
    request.session['half'] = True
    request.session['half_question'] = None
    request.session['half_wrong'] = None
    return render(request, "million/game.html", {
        "game": game,
        "questions": questions,
    })

def retire(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    questions = Question.objects.filter(game=game).order_by("value")
    prize = questions[request.session['question'] - 1].dollars()
    return render(request, "million/quit.html", {
        "game": game,
        "questions": questions,
        "prize": prize,
    })

def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    questions = Question.objects.filter(game=game).order_by("value")
    if request.session.get('game') != game.pk:
        request.session['game'] = game.pk
        request.session['question'] = 0
        request.session['call'] = True
        request.session['audience'] = True
        request.session['half'] = True
        request.session['half_question'] = None
        request.session['half_wrong'] = None
        return redirect(reverse("million-question", kwargs={"question_id": questions[request.session.get('question')].pk}))
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=request.POST.get('question'))
        if 'answer' in request.POST:
            answer = request.POST.get('answer')
            correct = ((answer == 'one' and question.answer_one_correct)
                or (answer == 'two' and question.answer_two_correct)
                or (answer == 'three' and question.answer_three_correct)
                or (answer == 'four' and question.answer_four_correct))
            prize = "$0"
            if correct:
                request.session['question'] += 1
            else:
                index = request.session['question']
                if index // 5:
                    prize = questions[(index // 5 * 5) - 1].dollars()
                request.session['question'] = 0
            if request.session['question'] >= len(questions):
                return render(request, "million/million.html", {
                    "prize": questions[len(questions)-1].dollars()
                })
            return render(request, "million/result.html", {
                "game": game,
                "prize": prize,
                "questions": questions,
                "question": question,
                "next_question": questions[request.session['question']],
                "correct": correct,
                "current": request.session['question'],
            })
        elif 'guess' in request.POST:
            guess = request.POST.get('guess')
            answer = getattr(question, "answer_%s" % guess)
            return render(request, "million/guess.html", {
                "game": game,
                "questions": questions,
                "question": question,
                "guess": guess,
                "answer": answer,
                "current": request.session['question'],
            })
    try:
        return redirect(reverse("million-question", kwargs={"question_id": questions[request.session.get('question')].pk}))
    except IndexError:
        return redirect(reverse("million-game", kwargs={"game_id": game.pk}))

def question(request, question_id, action=None):
    question = get_object_or_404(Question, pk=question_id)
    questions = Question.objects.filter(game=question.game).order_by("value")
    if action == 'call':
        request.session['call'] = False
    if action == 'half':
        request.session['half'] = False
        request.session['half_question'] = question.pk
    if action == 'audience':
        request.session['audience'] = False
    if request.session.get('half_question') == question.pk and request.session.get('half_wrong') is None:
        request.session['half_wrong'] = random.choice([num for num in ['one', 'two', 'three', 'four'] if not getattr(question, 'answer_%s_correct' % num)])
    return render(request, "million/question.html", {
        "game": question.game,
        "question": question,
        "questions": questions,
        "current": request.session['question'],
        "half": request.session['half'],
        "audience": request.session['audience'],
        "call": request.session['call'],
        "half_wrong": request.session.get('half_wrong') if request.session.get('half_question') == question.pk else None,
    })