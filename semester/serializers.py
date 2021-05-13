from rest_framework import serializers
from semester.models import Semester


class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = '__all__'
