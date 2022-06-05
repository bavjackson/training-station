import pytest
from pytest_django.asserts import assertTemplateUsed, assertRedirects

# Home view
def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")


def test_exercise_page_redirects_if_not_logged_in(client):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/users/login/?next=/workouts/exercises/")


def test_exercise_page_redirects_if_not_trainer(client, authenticated_user):
    response = client.get("/workouts/exercises/")
    assertRedirects(response, "/")


def test_exercise_page_loads_correct_html_if_trainer(client, authenticated_trainer):
    response = client.get("/workouts/exercises/")
    assertTemplateUsed(response, "exercises.html")
