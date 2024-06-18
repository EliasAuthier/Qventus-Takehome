from typing import List

from parts.controllers import BaseController
from parts.controllers.utils import word_ocurrence_map
from parts.models import Part

class PartController(BaseController):

    model_cls = Part

    def get_most_common_word_in_definitions(self):
        descriptions = Part.objects.values_list('description', flat=True)
        descriptions = ' '.join(descriptions)
        ocurrences = word_ocurrence_map(descriptions, only_top=5)
        return [word for word, _ocurr in ocurrences]