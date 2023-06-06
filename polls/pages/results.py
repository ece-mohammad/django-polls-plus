from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.utils import timezone
from django.views import generic


from ..models import Question
from .common import build_page



class ResultView(generic.DetailView):
    model         = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    """Show results for a question"""
    question = Question.objects.get(id=question_id)

    template = loader.get_template("polls/results.html")
    result_html = template.render({"question": question}, request)

    return HttpResponse(
        build_page(f"Question resaults | {question.id}", result_html, request)
    )



