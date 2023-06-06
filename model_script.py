#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.utils import timezone

from polls.models import Choice
from polls.models import Question

# question model -----------------------------------------------------------------
q = Question(question_text="Do you like python?", pub_date=timezone.now())

print(f">>> {q=}")
print(f">>> {q.question_text=}")
print(f">>> {q.pub_date}")
print(f">>> {q.id=}")
print(f">>> {q.was_published_recently()=}")

# choice model -------------------------------------------------------------------
ch = Choice(choice_text="No", question=q)
ch.save()

print(f">>> {ch=}")
print(f">>> {ch.id=}")
print(f">>> {ch.choice_text=}")
print(f">>> {ch.votes=}")
print(f">>> {ch.question=}")

# choice set ------------------------------------------------------------------
# q.choice_set.create(choice_text="No", votes=0)

print(f">>> {q.choice_set.all()=}")

# available questions
print(f">>> {Question.objects.all()=}")

# available choices
print(f">>> {Choice.objects.all()=}")


if __name__ == "__main__":
    ...

