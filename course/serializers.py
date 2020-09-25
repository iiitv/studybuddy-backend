from rest_framework import serializers
from course.models import Course, Assignment, ExamPaper, VideoLecture, Note

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
    
    def update(self, instance, validated_data):
        if instance.course_code != validated_data.get('course_code'):
            modified_course = Course(course_code=validated_data.get('course_code'),
                                     course_name=validated_data.get('course_name'),
                                     instructor=validated_data.get('instructor'))
            modified_course.save()
            try:
                course_assignment = Assignment.objects.filter(course=instance)
            except Assignment.DoesNotExist as exp:
                course_assignment = []
            try:
                course_exampaper = ExamPaper.objects.filter(course=instance)
            except ExamPaper.DoesNotExist as exp:
                course_exampaper = []
            try:
                course_videolecture = VideoLecture.objects.filter(course=instance)
            except VideoLecture.DoesNotExist as exp:
                course_exampaper = []
            for assignment in course_assignment:
                assignment.course = modified_course
                assignment.save()
                
            for exampaper in course_exampaper:
                exampaper.course = modified_course
                exampaper.save()
            for videolecture in course_videolecture:
                videolecture.course = modified_course
                videolecture.save()
            instance.delete()
            return super().update(modified_course, validated_data)
                
        return super().update(instance, validated_data)




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

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'