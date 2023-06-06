from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .models import Question, Choice


from .pages.index import IndexView
from .pages.details import DetailView
from .pages.results import ResultView
from .pages.vote import vote 
from .pages.add import QuestionAdd


# def build_page(title: str, body: str, request: HttpRequest) -> str:
#     """Build page from given fields (title, body, footer and HttpRequest)"""
#     page_template = loader.get_template("polls/base.html")
#     page_context = {
#         "title": title,
#         "body": body,
#     }
#
#     return page_template.render(page_context, request)
#
#
# class IndexView(generic.ListView):
#     """
#     List most recent questions 
#     """
#     model               = Question 
#     template_name       = "polls/index.html"
#     context_object_name = "latest_questions_list"
#     
#     MOST_RECENT_N: int  = 5
#
#     def get_queryset(self):
#         """get 5 most recent questions that have choices"""
#         # return Question.objects.order_by("-pub_date")[:self.MOST_RECENT_N]
#         questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
#         filtered_questions = [q for q in questions if q.choice_set.count() > 0]
#         return filtered_questions[:self.MOST_RECENT_N]
#
#
# class QuestionAdd(generic.CreateView):
#     model = Question
#     fields = [
#         "question_text"
#     ]
#     template_name = "polls/question_add.html"
#
#
# class DetailView(generic.DetailView):
#     model         = Question
#     template_name = "polls/details.html"
#
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# class ResultView(generic.DetailView):
#     model         = Question
#     template_name = "polls/results.html"
#
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# def results(request: HttpRequest, question_id: int) -> HttpResponse:
#     """Show results for a question"""
#     question = Question.objects.get(id=question_id)
#
#     template = loader.get_template("polls/results.html")
#     result_html = template.render({"question": question}, request)
#
#     return HttpResponse(
#         build_page(f"Question resaults | {question.id}", result_html, request)
#     )
#
#
# def vote(request: HttpRequest, question_id: int) -> HttpResponse:
#     """answer a question"""
#     question = get_object_or_404(Question, pk=question_id)
#
#     try:
#         selected_choice = Choice.objects.get(pk=request.POST["choice"])
#
#     except (KeyError, Choice.DoesNotExist):
#         return render(
#             request,
#             "polls/details.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't choose an answer!",
#             },
#         )
#
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse("polls:question-results", args=(question.id,)))
