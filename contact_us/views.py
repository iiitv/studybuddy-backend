from rest_framework.viewsets import ModelViewSet
from contact_us.models import Contact
from contact_us.serializers import ContactSerializers
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
class ContactViewSets(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

    