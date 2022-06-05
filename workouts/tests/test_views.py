import pytest
from pytest_django.asserts import assertTemplateUsed, assertRedirects
from workouts.models import Exercise

# Home view
def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")


def test_exercises_page_redirects_if_not_logged_in(client):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/users/login/?next=/workouts/exercises/")


def test_exercises_page_redirects_if_not_trainer(client, authenticated_user):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/")


def test_exercises_page_loads_correct_html_if_trainer(client, authenticated_trainer):
    response = client.get("/workouts/exercises/")
    assertTemplateUsed(response, "exercises.html")


def test_exercise_page_redirects_if_not_logged_in(client):
    response = client.get(f"/workouts/exercises/1/")
    assertRedirects(response, "/users/login/?next=/workouts/exercises/1/")


def test_exercise_page_redirects_if_not_trainer(client, authenticated_user):
    response = client.get(f"/workouts/exercises/1/")
    assertRedirects(response, "/")


def test_exercise_page_loads_correct_html_if_trainer(client, authenticated_trainer):
    exercise = Exercise.objects.create()

    response = client.get(f"/workouts/exercises/{exercise.id}/")
    assertTemplateUsed(response, "exercise.html")
