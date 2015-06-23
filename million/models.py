import time
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Game(models.Model):

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    name = models.CharField(max_length=50, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("million-game", kwargs={"game_id": self.pk})

def question_image_path(instance, filename):
    return ("million/{0}/{1}".format(time.strftime("%y"), filename.lower()))

class Question(models.Model):
    game = models.ForeignKey(Game, verbose_name=_('Game'))
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    picture = models.ImageField(null=True, blank=True, verbose_name=_('Picture'), upload_to=question_image_path)

    value = models.IntegerField(verbose_name=_('Value'))
    created = models.DateTimeField(auto_now_add=True)

    answer_one = models.CharField(max_length=50, verbose_name=_('First Answer'))
    answer_one_correct = models.BooleanField(verbose_name=_('First Answer is Correct'))

    answer_two = models.CharField(max_length=50, verbose_name=_('Second Answer'))
    answer_two_correct = models.BooleanField(verbose_name=_('Second Answer is Correct'))

    answer_three = models.CharField(max_length=50, verbose_name=_('Third Answer'))
    answer_three_correct = models.BooleanField(verbose_name=_('Third Answer is Correct'))

    answer_four = models.CharField(max_length=50, verbose_name=_('Fourth Answer'))
    answer_four_correct = models.BooleanField(verbose_name=_('Fourth Answer is Correct'))

    def get_absolute_url(self):
        return reverse("million-question", kwargs={"question_id": self.pk})


    def dollars(self):
        return "${:,}".format(self.value)

    def __unicode__(self):
        return u"{}: {} ${:,}".format(self.game, self.question, self.value)