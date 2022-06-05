from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from workouts.forms import ExerciseForm
from workouts.models import Exercise


def home_page(request):
    return render(request, "home.html")


@login_required
def exercises_page(request):
    trainer_group = Group.objects.get(name="Trainer")
    if trainer_group in request.user.groups.all():
        if request.method == "POST":
            print(request.POST["name"])
        exercises = Exercise.objects.all()
        form = ExerciseForm()
        return render(request, "exercises.html", {"form": form, "exercises": exercises})
    else:
        return redirect("/")


@login_required
def exercise_page(request, id):
    trainer_group = Group.objects.get(name="Trainer")
    if trainer_group in request.user.groups.all():
        return render(request, "exercise.html")
    else:
        return redirect("/")
