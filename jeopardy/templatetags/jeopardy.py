from django import template

register = template.Library()

@register.inclusion_tag('jeopardy/cell.html', takes_context=True)
def jeopardy_game_cell(context):
    game = context['game']
    topic = context['topic']
    point = context['point']
    questions_done = context['questions_done']
    return {
        "done": [topic.pk, point.pk] in questions_done,
        "game": game,
        "topic": topic,
        "point": point
    }