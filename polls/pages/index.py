from django.utils import timezone
from django.views import generic


from ..models import Question
from typing import Final


class IndexView(generic.ListView):
    """
    List most recent questions 
    """
    model               = Question 
    template_name       = "polls/index.html"
    context_object_name = "latest_questions_list"
    
    MOST_RECENT_N: Final[int] = 5
    MIN_QUESTION_CHOICES: Final[int] = 2

    def get_queryset(self):
        """get most recent MOST_RECENT_N questions that have at least MIN_QUESTION_CHOICES choices"""
        # return Question.objects.order_by("-pub_date")[:self.MOST_RECENT_N]
        questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
        filtered_questions = [q for q in questions if q.choice_set.count() >= self.MIN_QUESTION_CHOICES]
        return filtered_questions[:self.MOST_RECENT_N]


