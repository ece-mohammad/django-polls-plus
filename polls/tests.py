from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Question

from typing import *



# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        wwas_published_recently() must return False for 
        questions with pub_date in the future
        """
        future_time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_question = Question(
                pub_date=future_time
        )
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() must return True, when a 
        question was posted recently (< 24 hours ago)
        """
        now = timezone.now()
        recent_question = Question(
                pub_date=now - datetime.timedelta(hours=23, minutes=59, seconds=59)
        )
        self.assertIs(recent_question.was_published_recently(), True)
    
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() must return False for questions
        with pub_date older than 24 hours
        """
        now = timezone.now()
        old_question = Question(
                pub_date=now - datetime.timedelta(hours=24)
        )
        self.assertIs(old_question.was_published_recently(), False)


def create_question(question_text: str, choices: List[str], days: int) -> Question:
    question = Question.objects.create(
            question_text=question_text, 
            pub_date=timezone.now() + datetime.timedelta(days=days)
    )
    
    # add non empty choices
    for choice in filter(lambda x: bool(x), choices):
           question.choice_set.create(choice_text=choice, votes=0)

    return question


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        When no questions are added, display appropriate message
        message: "No questions are available at the moment"
        """
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions are available")
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])

    def test_question_with_no_choices(self):
        """
        Question with no choices is not displayed
        """
        old_question = create_question("old question", [], -1)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])

    def test_question_with_empty_string_choice(self):
        """
        Question with empty string as a choice is not displayed
        """
        old_question = create_question("old question", [""], -1)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])


    def test_old_question(self):
        """
        Old questions are displayed (pub_date < current date)
        """
        old_question = create_question("old question", ["foo", "bar"], -1)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, old_question.question_text)
        self.assertQuerySetEqual(response.context["latest_questions_list"], [old_question])

    def test_future_question(self):
        """
        Future questions are not displayed (pub_date > current date)
        """
        create_question("futrue question", ["foo", "bar"], 1)

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions are available")
        self.assertQuerySetEqual(response.context["latest_questions_list"], [])

    def test_multiple_old_questions(self):
        """
        Most recent N (5) questions are displayed
        """
        old_date = -1
        old_questions = [
                create_question(f"old question # {i}", ["foo", "bar"], old_date) for i in range(1, 11)
        ]

        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
                response.context["latest_questions_list"], 
                reversed(old_questions[5:])
        )

    def test_multiple_future_questions(self):
        """
        No future questions are displayed
        """
        future_date = 1
        future_questions = [
                create_question(f"future question {i}", ["foo", "bar"], future_date) for i in range(1, 11)
        ]

        response = self.client.get(reverse("polls:index"))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions are available")
        self.assertQuerySetEqual(
                response.context["latest_questions_list"],
                []
        )


    def test_display_only_old_questions(self):
        """
        When multiple old and future questions are added, onl display old questions
        """
        old_date = -1 
        future_date = 1

        old_questions = [
                create_question(f"old question # {i}", ["foo", "bar"], old_date) for i in range(1, 11)
        ]

        future_questions = [
                create_question(f"future question {i}", ["foo", "bar"], future_date) for i in range(1, 11)
        ]

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(
                response.context["latest_questions_list"], 
                reversed(old_questions[5:])
        )


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        Future questions should have no details
        """
        future_date = 1
        future_question = create_question("future question", ["foo", "bar"], future_date)

        response = self.client.get(reverse("polls:question-details", args=(future_question.id,)))
        
        self.assertEqual(response.status_code, 404)

    def test_old_question(self):
        """
        Display old question details
        """
        old_date = -1
        old_question = create_question("old question", ["foo", "bar"], old_date)
        
        response = self.client.get(reverse("polls:question-details", args=(old_question.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, old_question.question_text)


class QuestionResultViewTest(TestCase):
    def test_future_question(self):
        """
        Future questions should have no results
        """
        future_date = 1
        future_question = create_question("future question", ["foo", "bar"], future_date)

        response = self.client.get(reverse("polls:question-results", args=(future_question.id,)))
        
        self.assertEqual(response.status_code, 404)

    def test_old_question(self):
        """
        Display old question results
        """
        old_date = -1
        old_question = create_question("old question", ["foo", "bar"], old_date)
        
        response = self.client.get(reverse("polls:question-results", args=(old_question.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, old_question.question_text)


