from rest_framework.viewsets import ModelViewSet
from course.models import Course, Assignment, ExamPaper, VideoLecture
from course.serializers import CourseSerializers, AssignmentSerializers, ExamPaperSerializers, VideoLectureSerializers 

class CourseViewSets(ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class AssignmentViewSets(ModelViewSet):
    serializer_class = AssignmentSerializers
    queryset = Assignment.objects.all()


class ExamPaperViewSets(ModelViewSet):
    serializer_class = ExamPaperSerializers
    queryset = ExamPaper.objects.all()


class VideoLectureViewSets(ModelViewSet):
    serializer_class = VideoLectureSerializers
    queryset = VideoLecture.objects.all()
