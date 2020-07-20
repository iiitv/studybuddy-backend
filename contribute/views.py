from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from contribute.models import Contribute
from contribute.serializers import ContributeSerializers

class ContributeViewSets(ModelViewSet):
    serializer_class = ContributeSerializers
    queryset = Contribute.objects.all()