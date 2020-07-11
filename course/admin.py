from django.contrib import admin
from course.models import Course, Assignment, ExamPaper

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(ExamPaper)
