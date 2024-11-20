from django.urls import path

from . import views

urlpatterns = [
    path("resume/", views.postResume, name="postResume"),
    path("post-skills/", views.postChosenSkills, name="postSkills")
]