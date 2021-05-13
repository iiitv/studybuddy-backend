from django.db import models


class Semester(models.Model):
    semester = models.CharField(max_length=8)
    details = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.semester}'
