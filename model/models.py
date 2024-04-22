from django.db import models


# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.is_completed}'


class User(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=10, blank=False)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.email}"
