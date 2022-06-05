from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, "home.html")


@login_required
def exercises_page(request):
    print(request.user)
    trainer_group = Group.objects.get(name="Trainer")
    if trainer_group in request.user.groups.all():
        return render(request, "exercises.html")
    else:
        return redirect("/")


@login_required
def exercise_page(request, id):
    print(request.user)
    trainer_group = Group.objects.get(name="Trainer")
    if trainer_group in request.user.groups.all():
        return render(request, "exercise.html")
    else:
        return redirect("/")
