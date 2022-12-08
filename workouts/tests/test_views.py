import pytest
from pytest_django.asserts import (
    assertTemplateUsed,
    assertRedirects,
    assertContains,
    assertJSONEqual,
)
from model_bakery import baker
from django.forms import model_to_dict

from workouts.forms import ExerciseForm
from workouts.models import Exercise

# Home view
def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")


# Multiple exercises view
def test_exercises_page_redirects_if_not_logged_in(client):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/users/login/?next=/workouts/exercises/")


def test_exercises_page_redirects_if_not_trainer(client, authenticated_user):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/")


def test_exercises_page_loads_correct_html_if_trainer(client, authenticated_trainer):
    response = client.get("/workouts/exercises/")
    assertTemplateUsed(response, "exercises.html")


def test_exercises_page_uses_correct_form(client, authenticated_trainer):
    response = client.get("/workouts/exercises/")
    assert isinstance(response.context["form"], ExerciseForm)


def test_passes_exercises_to_template(client, authenticated_trainer):
    exercises = baker.make(Exercise, _quantity=3)
    response = client.get("/workouts/exercises/")
    assert list(response.context["exercises"]) == exercises


def test_displays_all_exercises(client, authenticated_trainer):
    exercises = baker.make(Exercise, _quantity=3, _fill_optional=True)
    response = client.get("/workouts/exercises/")

    assertContains(response, exercises[0].name)
    assertContains(response, exercises[1].name)
    assertContains(response, exercises[2].name)


def test_creates_exercise_when_submitting_valid_form(client, authenticated_trainer):
    exercise = model_to_dict(baker.prepare(Exercise, _fill_optional=True))
    del exercise["id"]
    response = client.post("/workouts/exercises/", exercise)

    db_exercise = Exercise.objects.first()

    assert db_exercise.name == exercise["name"]


def test_returns_new_exercise_after_submitting_valid_form(
    client, authenticated_trainer
):
    exercise = model_to_dict(baker.prepare(Exercise, _fill_optional=True))
    del exercise["id"]
    response = client.post("/workouts/exercises/", exercise)

    assertJSONEqual(response.content, exercise)


def test_throws_error_when_posting_invalid_data(client, authenticated_trainer):
    response = client.post("/workouts/exercises/", {"name": ""})

    assert response.status_code == 400


# Single exercise view
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
