from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from parts.models import Part
from parts.serializers import PartSerializer, TopDescriptionWordsSerializer
from parts.controllers import PartController
from parts.views import BaseViewSet


class PartViewSet(BaseViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    controller = PartController()

    @action(methods=['GET'], detail=False)
    def top_description_words(self, request: Request):
        words = self.controller.get_most_common_word_in_definitions()
        print(words)
        serialized = TopDescriptionWordsSerializer(data={'words': words})
        serialized.is_valid()

        return Response(serialized.data)