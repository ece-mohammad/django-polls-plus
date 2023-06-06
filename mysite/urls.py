"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.contrib.admin.sites import import_string
from django.urls import path, include
from polls import views as polls_views


urlpatterns = [
    # home page
    path("",            polls_views.IndexView.as_view(), name="home"),

    # admin 
    path("admin/",      admin.site.urls),

    # sign up 
    path("accounts/",   include("accounts.urls")),

    # log in/ log out/ password reset
    path("accounts/",   include("django.contrib.auth.urls")),

    # polls 
    path("polls/",      include("polls.urls")),

    # debug_toolbar
    path("__debug__/",  include("debug_toolbar.urls")),
]
