from django.urls import path
from workouts import views

urlpatterns = [
    path("exercises/", views.exercises_page, name="exercises"),
    path("exercises/<int:id>/", views.exercise_page, name="exercise"),
]
