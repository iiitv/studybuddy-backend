from django.db import models
from semester.models import Semester
from course.models import Course


class Contact(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=20)
    suggestion = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.name} {self.field}'