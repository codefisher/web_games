import time
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

def question_image_path(instance, filename):
    return ("jeopardy/{0}/{1}".format(time.strftime("%y"), filename.lower()))

class Game(models.Model):

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    name = models.CharField(max_length=50, verbose_name=_('Name'))
    win_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture At Victory'),
        upload_to=question_image_path)
    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jeopardy-game", kwargs={"game_id": self.pk})

class BonusQuestion(models.Model):

    class Meta:
        verbose_name = _('Final Question')
        verbose_name_plural = _('Final Question')

    game = models.ForeignKey(
        Game, verbose_name=_('Game'), related_name="bonus_question")
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture'),
        upload_to=question_image_path)
    sound = models.FileField(
        null=True, blank=True, verbose_name=_('Sound'),
        upload_to=question_image_path)
    answer = models.CharField(max_length=255, verbose_name=_('Answer'))
    value = models.IntegerField(verbose_name=_('Points'))

    correct_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture When Correct'),
        upload_to=question_image_path)
    wrong_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture When Wrong'),
        upload_to=question_image_path)

    def __unicode__(self):
        return self.question

class Points(models.Model):

    class Meta:
        verbose_name = _('Points')
        verbose_name_plural = _('Points')

    game = models.ForeignKey(
        Game, verbose_name=_('Game'), related_name="points")
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

class Topic(models.Model):
    game = models.ForeignKey(
        Game, verbose_name=_('Game'), related_name="topic")
    name = models.CharField(max_length=50, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name

class Question(models.Model):

    game = models.ForeignKey(
        Game, verbose_name=_('Game'), related_name="questions")
    points = models.ForeignKey(
        Points, null=True, verbose_name=_('Points'), related_name="points")
    topic = models.ForeignKey(
        Topic, null=True, verbose_name=_('Topic'), related_name="topic")
    question = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('Question'))
    picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture'),
        upload_to=question_image_path)
    sound = models.FileField(
        null=True, blank=True, verbose_name=_('Sound'),
        upload_to=question_image_path)
    answer = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_('Answer'))
    bonus = models.IntegerField(default=0, verbose_name=_('Bonus Points'))

    correct_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture When Correct'),
        upload_to=question_image_path)
    wrong_picture = models.ImageField(
        null=True, blank=True, verbose_name=_('Picture When Wrong'),
        upload_to=question_image_path)


    def __unicode__(self):
        if self.question:
            return self.question
        return unicode(_(u'Question'))
