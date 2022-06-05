from django import forms

from workouts.models import Exercise


class ExerciseForm(forms.models.ModelForm):
    class Meta:
        model = Exercise
