from rest_framework import serializers
from contribute.models import Contribute

class ContributeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contribute
        fields = '__all__'