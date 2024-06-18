from django.urls import reverse
from parts.tests import BaseIntegrationTest
from parts.models import Part
from rest_framework import status

class PartActionEndpointsTest(BaseIntegrationTest):
    

    def test_top_description_words_endpoints(self):
        url = reverse('part-top-description-words')
        descriptions = ' '.join(Part.objects.values_list('description', flat=True))
        descriptions = set(descriptions.split(' '))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for word in response.json().get('words'):
            self.assertIn(word, descriptions)

