from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("million-game", kwargs={"game_id": self.pk})


class Question(models.Model):
    game = models.ForeignKey(Game)
    question = models.CharField(max_length=255)

    value = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    answer_one = models.CharField(max_length=50)
    answer_one_correct = models.BooleanField()

    answer_two = models.CharField(max_length=50)
    answer_two_correct = models.BooleanField()

    answer_three = models.CharField(max_length=50)
    answer_three_correct = models.BooleanField()

    answer_four = models.CharField(max_length=50)
    answer_four_correct = models.BooleanField()

    def get_absolute_url(self):
        return reverse("million-question", kwargs={"question_id": self.pk})


    def dollars(self):
        return "${:,}".format(self.value)

    def __str__(self):
        return "{}: {} ${:,}".format(self.game, self.question, self.value)