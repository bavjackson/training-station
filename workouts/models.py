from django.db import models
from django.urls import reverse


class Exercise(models.Model):
    def get_absolute_url(self):
        return reverse("view_exercise", args=[self.id])
