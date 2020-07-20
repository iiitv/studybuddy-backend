from rest_framework import serializers
from course.models import Course, Assignment, ExamPaper, VideoLecture

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class AssignmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = '__all__'


class ExamPaperSerializers(serializers.ModelSerializer):

    class Meta:
        model = ExamPaper
        fields = '__all__'

class VideoLectureSerializers(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = '__all__'