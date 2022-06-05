from django.urls import path
from workouts import views

urlpatterns = [path("exercises/", views.exercises_page, name="exercises")]
