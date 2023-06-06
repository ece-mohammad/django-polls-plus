from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse


from ..models import Question, Choice

from .common import build_page


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """answer a question"""
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = Choice.objects.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't choose an answer!",
            },
        )

    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:question-results", args=(question.id,)))
