from django.contrib import admin
from course.models import Course, Assignment, ExamPaper, VideoLecture, Note

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(ExamPaper)
admin.site.register(VideoLecture)
admin.site.register(Note)
