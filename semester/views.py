from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from semester.models import Semester
from semester.serializers import SemesterSerializer

class SemesterViewSets(ModelViewSet):
    serializer_class = SemesterSerializer
    queryset = Semester.objects.all()