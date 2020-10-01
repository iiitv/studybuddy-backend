from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from semester.models import Semester
from semester.serializers import SemesterSerializers


class SemesterViewSets(ModelViewSet):
    serializer_class = SemesterSerializers
    queryset = Semester.objects.all()
