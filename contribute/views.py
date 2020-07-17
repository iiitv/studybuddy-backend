from django.shortcuts import render
from rest_framework.viewsets import ModelViewSets
from contribute.models import Contribute
from contribute.serializers import ContributeSerializers

class ContributeViewSets(ModelViewSets):
    serializer_class = ContributeSerializers
    queryset = Contribute.objects.all()