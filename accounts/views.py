from django.forms.fields import EmailField, CharField
from django.shortcuts import render
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField
from django.contrib.auth.admin import User
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class UserSignUpForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email"
        ]

        field_classes = {
            "username":   UsernameField,
            "first_name": CharField,
            "last_name":  CharField,
            "email":      EmailField
        }


class SignUpView(generic.CreateView):
    form_class    = UserSignUpForm
    success_url   = reverse_lazy("login")
    template_name = "registration/signup.html"


# class UserView(generic.DetailView):
#     model         = User 
#     template_name = "accounts/profile.html"
#
#     def get_queryset(self):
#         return User.objects.filter(username__startswith=self.slug)
 
