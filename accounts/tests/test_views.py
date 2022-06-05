import pytest
from pytest_django.asserts import assertTemplateUsed

# Home view
def test_login_page_returns_correct_html(client):
    response = client.get("/accounts/login/")
    assertTemplateUsed(response, "registration/login.html")


def test_profile_page_returns_correct_html(client):
    response = client.get("/accounts/profile/")
    assertTemplateUsed(response, "profile.html")
