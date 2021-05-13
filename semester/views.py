from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from semester.models import Semester
from semester.serializers import SemesterSerializers
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated


class SemesterViewSets(ModelViewSet):
    permission_classes =[IsAuthenticated]
    serializer_class = SemesterSerializers
    queryset = Semester.objects.all()
