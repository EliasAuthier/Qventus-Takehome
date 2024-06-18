from parts.tests import BaseUnitTest
from parts.controllers import PartController
from parts.models import Part

class PartControllerTest(BaseUnitTest):

    controller_cls = PartController

    def setUp(self) -> None:
        number_of_parts = 5
        for i in range(number_of_parts):
            Part.objects.create(
                name = 'name_' + str(i), 
                sku = 'sku_' + str(i), 
                description = 'description ' + str(i), 
                weight_ounces = i, 
                is_active = i%2)
        return super().setUp()
            
    def tearDown(self) -> None:
        Part.objects.all().delete()
        return super().tearDown()


    def test_get_most_common_word_in_definitions(self):
        manager = PartController()
        words = manager.get_most_common_word_in_definitions()
        self.assertEqual(words[0], 'description')