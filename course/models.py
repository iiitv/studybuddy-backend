from django.db import models

def get_upload_path_assignment(instance, filename):
    return 'Assignment_{0}/{1}'.format(instance.course.course_code, filename)

def get_upload_path_exam(instance, filename):
    return 'Exam_{0}/{1}'.format(instance.course.course_code, filename)

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.course_code}'

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    attachment = models.FileField(upload_to=get_upload_path_assignment)

    def __str__(self):
        return f'{self.heading}'

class ExamPaper(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    attachment = models.FileField(upload_to=get_upload_path_exam)

    def __str__(self):
        return f'{self.heading}'
