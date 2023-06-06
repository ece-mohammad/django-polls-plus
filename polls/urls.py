from django.urls import path, include

from . import views

app_name = "polls"

question_id_patterns = [
        path("",         views.DetailView.as_view(), name="question-details"),
        path("results/", views.ResultView.as_view(), name="question-results"),
]


urlpatterns = [
        path("",                        views.IndexView.as_view(),   name="index"),
        path("<int:question_id>/vote/", views.vote,                  name="question-vote"),
        path("add/",                    views.QuestionAdd.as_view(), name="question-add"),
        # path("add/",                    views.QuestionAdd,           name="question-add"),

        path("<int:pk>/", include(question_id_patterns)),
]

