from rest_framework import serializers
from contact_us.models import Contact

class ContactSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'