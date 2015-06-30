from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import BonusQuestion, Game, Points, Question, Topic

class TopicInline(admin.TabularInline):
    model = Topic

    def get_extra(self, request, obj=None, **kwargs):
        extra = 5
        if obj:
            return extra - obj.topic.count()
        return extra


class PointsInline(admin.TabularInline):
    model = Points

    def get_extra(self, request, obj=None, **kwargs):
        extra = 5
        if obj:
            return extra - obj.points.count()
        return extra

class QuestionInlineFormSet(forms.models.BaseInlineFormSet):
    model = Question

    def __init__(self, *args, **kwargs):
        super(QuestionInlineFormSet, self).__init__(*args, **kwargs)
        game = kwargs['instance']
        points = Points.objects.filter(game=game.pk)
        topics = Topic.objects.filter(game=game.pk)
        initial = []
        for topic in topics:
            for point in points:
                if not Question.objects.filter(points=point.pk, topic=topic.pk).count():
                    initial.append({'points': point, 'topic': topic})
        self.initial = initial

class QuestionInline(admin.StackedInline):
    model = Question
    formset = QuestionInlineFormSet

    fields = ['game', 'topic', 'points',
              'question', 'answer', 'picture', 'sound', 'bonus',
              'correct_picture', 'wrong_picture']

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return (obj.points.count() * obj.topic.count()) - obj.questions.count()
        return 0

class BonusQuestionInline(admin.StackedInline):
    model = BonusQuestion

    fields = ['question', 'answer', 'picture', 'sound', 'value',
              'correct_picture', 'wrong_picture']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2
        if obj:
            return extra - obj.bonus_question.count()
        return extra



class GameAdmin(admin.ModelAdmin):
    list_display = ["name"]

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(GameAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [TopicInline, PointsInline, QuestionInline, BonusQuestionInline]
        return super(GameAdmin, self).change_view(*args, **kwargs)

admin.site.register(Game, GameAdmin)

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['game', 'points', 'topic', 'question', 'picture',
                  'correct_picture', 'wrong_picture', 'sound', 'answer', 'bonus']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'game'):
            self.fields['points'].queryset = Points.objects.filter(game=self.instance.game.pk)
            self.fields['topic'].queryset = Topic.objects.filter(game=self.instance.game.pk)

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

    list_filter = ["game"]
    list_display = ["game", "topic", "points", "question", "answer", "bonus"]

    fields = ['game', 'topic', 'points',
              'question', 'answer', 'picture', 'sound', 'bonus'
              'correct_picture', 'wrong_picture']

    def get_fieldsets(self, request, obj=None, **kwargs):
        if obj:
            return (
                (None, {
                    'fields': ('game', 'topic', 'points')
                }),
                (_('Question'), {
                    'fields': ('question', 'answer', 'picture', 'sound', 'bonus')
                }),
                (_('Images'), {
                    'fields': ('correct_picture', 'wrong_picture',)
                }),
            )
        else:
            return super(QuestionAdmin, self).get_fieldsets(request, obj, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            pass
        else:
            kwargs['fields'] = ['game']
        return super(QuestionAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Question, QuestionAdmin)


