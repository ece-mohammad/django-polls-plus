import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User, AnonymousUser


# Create your models here.
class Question(models.Model):
    question_text = models.CharField("question text", max_length=200)
    pub_date      = models.DateTimeField("date published")
    # author        = models.ForeignKey(User, on_delete=models.CASCADE)

    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published recently?"
    )
    def was_published_recently(self) -> bool:
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date <= now

    def __str__(self) -> str:
        return f"{self.question_text}"


class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("choice text", max_length=200)
    votes       = models.IntegerField("votes", default=0)

    def __str__(self) -> str:
        return f"{self.choice_text}"


