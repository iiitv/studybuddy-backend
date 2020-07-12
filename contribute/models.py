from django.db import models
from course.models import Course
from semester.models import Semester

def get_upload_path_contribute(instance, filename):
    return 'Contribute_{0}/{1}'.format(instance.course.course_code, filename)

class Contribute(models.Model):
    name = models.CharField(max_length=100)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    field = models.CharField(max_length=20)
    attachment = models.FileField(upload_to=get_upload_path_contribute)
    reason = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.course.course_code} {self.field}'

