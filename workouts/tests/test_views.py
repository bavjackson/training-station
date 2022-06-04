import pytest
from pytest_django.asserts import assertTemplateUsed

# Home view
def test_home_page_returns_correct_html(client):
    response = client.get("/")
    assertTemplateUsed(response, "home.html")
