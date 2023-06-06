from django.urls import path,include, re_path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/",     views.SignUpView.as_view(), name="signup" ),
    # path("<str:slug>/", views.UserView.as_view(),   name="profile"),
]
