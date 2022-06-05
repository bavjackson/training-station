from django import forms

from workouts.models import Exercise

EMPTY_NAME_ERROR = "Exercise must have a name"


class ExerciseForm(forms.models.ModelForm):
    class Meta:
        model = Exercise
        fields = ("name",)
        widgets = {"name": forms.fields.TextInput(attrs={"id": "id_exercise_name"})}
        error_messages = {"name": {"required": EMPTY_NAME_ERROR}}
