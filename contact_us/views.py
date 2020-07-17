from rest_framework.viewsets import ModelViewSet
from contact_us.models import Contact
from contact_us.serializers import ContactSerializers

class ContactViewSets(ModelViewSet):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

    