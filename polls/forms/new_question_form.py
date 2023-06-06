from django import forms 
from django.utils import timezone

from ..models import Question, Choice


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            "question_text"
        ]    
    
    choice1 = forms.CharField(max_length=200)
    choice2 = forms.CharField(max_length=200)
    
    def save(self, commit=True):
        question = super().save(commit=False)
        if not commit:
            return question
        

        
        # add pub_date
        question.pub_date = timezone.now()
        # TODO: add author
        # self.get_context()["user"] # ???
        question.save()
        
        # get choices
        choices = [ self.cleaned_data.get(f"choice{i}") for i in (1, 2) ]
        for choice in choices:
            Choice(question=question, choice_text=choice, votes=0).save()
        
        return question


    # ChoiceFormSet = forms.modelformset_factory(
    #     Choice, 
    #     fields       = ["choice_text"],
    #     extra        = 2,
    #     max_num      = 10,
    #     validate_max = True,
    # )
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.choice_formset = self.ChoiceFormSet(*args, **kwargs)
    #
    # def is_valid(self):
    #     return super().is_valid and self.choice_formset.is_valid
    #
    # def save(self, commit=True):
    #     question = super().save(commit=False)
    #     if not commit:
    #         return question
    #
    #     question.pub_date = timezone.now()
    #     
    #     for form in self.choice_formset:
    #         if form.is_valid:
    #             choice = form.save(commit=False)
    #             choice.question = question
    #             choice.save()
    #     
    #     question.save()
    #     return question


