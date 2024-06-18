from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase


class BaseUnitTest(TestCase):
    
    pass

class BaseIntegrationTest(APITestCase):
    
    def get_absolute_url(self, url_name: str, kwargs) -> str:
        relative_url = reverse(url_name, kwargs=kwargs)
        return 'http://testserver' + relative_url