import json
from django.test import TestCase
from rest_framework import status


class ClientTestCase(TestCase):
    def test_client_list(self):
        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_detail(self):
        response = self.client.get('/clients/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_create(self):
        response = self.client.post('/clients/', {
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Main',
            'date_of_birth': '2020-01-01'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_update(self):
        response = self.client.put(
            '/clients/1/',
            json.dumps({
                "id": 1,
                'first_name': 'John',
                'last_name': 'Doe',
                'address': '123 Main',
                'date_of_birth': '2020-01-01'
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_delete(self):
        response = self.client.delete('/clients/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
