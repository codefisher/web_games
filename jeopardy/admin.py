from django.contrib import admin
from django import forms
from .models import BonusQuestion, Game, Points, Question, Topic

class TopicInline(admin.TabularInline):
    model = Topic
    min_num = 5
    extra = 0

class PointsInline(admin.TabularInline):
    model = Points
    min_num = 5
    extra = 0

class BonusQuestionInline(admin.TabularInline):
    model = BonusQuestion
    min_num = 2
    extra = 0

class GameAdmin(admin.ModelAdmin):
    list_display = ["name"]

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(GameAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [TopicInline, PointsInline, BonusQuestionInline]
        return super(GameAdmin, self).change_view(*args, **kwargs)

admin.site.register(Game, GameAdmin)

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['game', 'points', 'topic', 'question', 'answer', 'bonus']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'game'):
            self.fields['points'].queryset = Points.objects.filter(game=self.instance.game.pk)
            self.fields['topic'].queryset = Topic.objects.filter(game=self.instance.game.pk)

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm

    list_filter = ["game"]
    list_display = ["game", "topic", "points", "question", "answer", "bonus"]

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            pass
        else:
            kwargs['fields'] = ['game']
        return super(QuestionAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Question, QuestionAdmin)


