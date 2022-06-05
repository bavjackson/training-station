import pytest
from pytest_django.asserts import assertTemplateUsed, assertRedirects

# Home view
def test_login_page_returns_correct_html(client):
    response = client.get("/users/login/")
    assertTemplateUsed(response, "registration/login.html")


def test_profile_page_returns_correct_html_if_logged_in(client, authenticated_user):
    response = client.get("/users/profile/")
    assertTemplateUsed(response, "profile.html")


def test_profile_page_redirects_if_not_logged_in(client):
    response = client.get("/users/profile/")
    assertRedirects(response, "/")
