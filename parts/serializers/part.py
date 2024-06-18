from rest_framework.serializers import Serializer, ListField, CharField
from parts.models import Part
from parts.serializers import BaseSerializer

class PartSerializer(BaseSerializer):

    class Meta:
        model = Part
        fields = '__all__'


class TopDescriptionWordsSerializer(Serializer):
    words = ListField(child=CharField())