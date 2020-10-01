from rest_framework.viewsets import ModelViewSet
from course.models import Course, Assignment, ExamPaper, VideoLecture
from course.serializers import CourseSerializers, AssignmentSerializers, ExamPaperSerializers, VideoLectureSerializers 
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Assignment, ExamPaper, VideoLecture, Note
from course.serializers import CourseSerializers, AssignmentSerializers, ExamPaperSerializers, VideoLectureSerializers, NoteSerializers 

class CourseViewSets(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class AssignmentViewSets(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = AssignmentSerializers
    queryset = Assignment.objects.all()


class ExamPaperViewSets(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = ExamPaperSerializers
    queryset = ExamPaper.objects.all()


class VideoLectureViewSets(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = VideoLectureSerializers
    queryset = VideoLecture.objects.all()

class NoteViewSets(ModelViewSet):
    serializer_class = NoteSerializers
    queryset = Note.objects.all()
