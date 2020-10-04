from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from contribute.models import Contribute
from contribute.serializers import ContributeSerializers
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
class ContributeViewSets(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class = ContributeSerializers
    queryset = Contribute.objects.all()