import pytest
from pytest_django.asserts import assertContains

from workouts.forms import ExerciseForm, EMPTY_NAME_ERROR


def test_form_validation_for_blank_exercise_name():
    form = ExerciseForm(data={"name": ""})
    assert not form.is_valid()
    assert form.errors["name"] == [EMPTY_NAME_ERROR]
