from django import forms
from django.http import HttpResponse
from django.utils.timezone import timezone 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..models import Question, Choice 
from ..forms.new_question_form import NewQuestionForm


class QuestionAdd(CreateView):
    model         = Question 
    form_class    = NewQuestionForm
    template_name = "polls/question_add.html"
    success_url   = reverse_lazy("polls:index")

    # def form_valid(self, form: NewQuestionForm) -> HttpResponse:
    #     form.instance.author = self.request.user
    #     response = super().form_valid(form)
    #     form.instance_choice_set.set(form.choice_formset.save())
    #     return response
    # 
    # def form_invalid(self, form: NewQuestionForm) -> HttpResponse:
    #     response = super().form_invalid(form)
    #     choice_formset = form.choice_formset
    #     if choice_formset.is_bound:
    #         response.context_data['choice_formset'] = choice_formset
    #     return response
    #
    # def get_context_data(self, **kwargs) -> dict:
    #     if 'choice_formset' not in kwargs:
    #         kwargs['choice_formset'] = self.form_class.ChoiceFormSet()
    #     return super().get_context_data(**kwargs)



