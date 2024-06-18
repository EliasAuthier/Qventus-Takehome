from django.urls import reverse
from rest_framework import status
from parts.models import Part
from parts.tests import BaseIntegrationTest

class PartCRUDEndpointsTest(BaseIntegrationTest):

    def setUp(self):
        self.part1 = Part.objects.create(
            name="Test PartName 1", 
            sku="Test Sku 1", 
            description="Test Description 1 Tightly wound nickel-gravy alloy spring", 
            weight_ounces=11, 
            is_active=True
        )
        self.part2 = Part.objects.create(
            name="Test PartName 2", 
            sku="Test Sku 2", 
            description="Test Description 2 Tightly wound nickel-gravy alloy spring", 
            weight_ounces=22, 
            is_active=True
        )

    @property
    def new_part_data(self):
        return {
            "name": "new_name",
            "sku": "new_sku",
            "description": "new_description",
            "weight_ounces": 100,
            "is_active": False,
        }


    def test_get_parts(self):
        url = reverse('part-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {
                "url": self.get_absolute_url('part-detail', kwargs={'pk': part.id}),
                "id": part.id,
                "name": part.name,
                "sku": part.sku,
                "description": part.description,
                "weight_ounces": part.weight_ounces,
                "is_active": part.is_active,
            }
            for part in [self.part1, self.part2]
        ]
        response_data = response.json()['results']
        for part_data in expected_data:
            self.assertIn(part_data, response_data)

    def test_get_part(self):
        part = self.part1
        url = reverse('part-detail', kwargs={'pk': part.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "url": self.get_absolute_url('part-detail', kwargs={'pk': part.id}),
            "id": part.id,
            "name": part.name,
            "sku": part.sku,
            "description": part.description,
            "weight_ounces": part.weight_ounces,
            "is_active": part.is_active,
        }
        self.assertDictEqual(response.json(), expected_data)

    def test_post_part(self):
        original_part_count = Part.objects.count()
        new_part_data = self.new_part_data
        url = reverse('part-list')
        response = self.client.post(url, data=new_part_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        id = response_data.get('id', None)
        expected_data = {
            "url": self.get_absolute_url('part-detail', kwargs={'pk': id}),
            "id": id,
            "name": "new_name",
            "sku": "new_sku",
            "description": "new_description",
            "weight_ounces": 100,
            "is_active": False,
        }
        self.assertDictEqual(response.json(), expected_data)
        self.assertEqual(Part.objects.count(), original_part_count + 1)

    def test_post_part_missing_field_failure(self):
        original_part_count = Part.objects.count()
        new_part_data = self.new_part_data
        new_part_data.pop('name')
        url = reverse('part-list')
        response = self.client.post(url, data=new_part_data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertIn('name', response_data.keys())
        self.assertEqual(Part.objects.count(), original_part_count)

    def test_put_part(self):
        original_part_count = Part.objects.count()
        part = self.part1
        url = reverse('part-detail', kwargs={'pk': part.id})
        new_part_data = self.new_part_data
        response = self.client.put(url, data=new_part_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "url": self.get_absolute_url('part-detail', kwargs={'pk': part.id}),
            "id": part.id,
            "name": "new_name",
            "sku": "new_sku",
            "description": "new_description",
            "weight_ounces": 100,
            "is_active": False,
        }
        self.assertDictEqual(response.json(), expected_data)
        self.assertEqual(Part.objects.count(), original_part_count)
        expected_data.pop('url')
        part = Part.objects.get(id = part.id)
        for key in expected_data.keys():
            self.assertEqual(expected_data[key], getattr(part, key))

    def test_patch_part(self):
        original_part_count = Part.objects.count()
        part = self.part1
        url = reverse('part-detail', kwargs={'pk': part.id})
        new_part_data = {
            "name": "new_name"
        }
        response = self.client.patch(url, data=new_part_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "url": self.get_absolute_url('part-detail', kwargs={'pk': part.id}),
            "id": part.id,
            "name": "new_name",
            "sku": part.sku,
            "description": part.description,
            "weight_ounces": part.weight_ounces,
            "is_active": part.is_active,
        }
        self.assertDictEqual(response.json(), expected_data)
        self.assertEqual(Part.objects.count(), original_part_count)
        expected_data.pop('url')
        part = Part.objects.get(id = part.id)
        self.assertEqual(expected_data['name'], 'new_name')

    def test_delete_part(self):
        original_part_count = Part.objects.count()
        part = self.part1
        url = reverse('part-detail', kwargs={'pk': part.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Part.objects.count(), original_part_count - 1)
        with self.assertRaises(Exception) as e:
            Part.objects.get(id=part.id)
