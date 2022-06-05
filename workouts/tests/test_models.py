import pytest
from workouts.models import Exercise


def test_saving_and_retrieving_exercise():
    first_exercise = Exercise()
    first_exercise.save()

    second_exercise = Exercise()
    second_exercise.save()

    saved_exercise = Exercise.objects.first()
    assert saved_exercise == first_exercise

    saved_exercises = Exercise.objects.all()
    assert saved_exercises.count() == 2
    assert saved_exercises[0] == first_exercise
    assert saved_exercises[1] == second_exercise
