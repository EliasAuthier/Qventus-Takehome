from rest_framework.serializers import HyperlinkedModelSerializer, IntegerField


class BaseSerializer(HyperlinkedModelSerializer):
    id = IntegerField(read_only=True)