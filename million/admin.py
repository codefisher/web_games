from django.contrib import admin
from .models import Game, Question

class GameAdmin(admin.ModelAdmin):
    pass
admin.site.register(Game, GameAdmin)

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('game', 'question', 'value')

    fieldsets = (
        (None, {
            'fields': ('game', 'question', 'value')
        }),
        ('First Question', {
            'fields': ('answer_one', 'answer_one_correct',)
        }),
        ('Second Question', {
            'fields': ('answer_two', 'answer_two_correct',)
        }),
        ('Third Question', {
            'fields': ('answer_three', 'answer_three_correct',)
        }),
        ('Fourth Question', {
            'fields': ('answer_four', 'answer_four_correct',)
        }),
    )

admin.site.register(Question, QuestionAdmin)