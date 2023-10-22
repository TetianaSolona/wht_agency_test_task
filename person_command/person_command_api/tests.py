from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Command, Person

"""
Tests for Command.
"""


class CommandViewSetTestCase(APITestCase):
    def setUp(self):
        self.command_data_main = {'name': 'test_command'}
        self.command = Command.objects.create(**self.command_data_main)
        self.url = 'http://127.0.0.1:8000/command/'

    def test_create_command(self):
        self.command_data = {'name': 'test_command_2'}
        response = self.client.post(self.url, self.command_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=f'Create command should return 201 status code. Error: {response.content}')

    def test_retrieve_command(self):
        response = self.client.get(reverse('command-detail', args=[self.command.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Retrieve command should return 200 status code. Error: {response.content}')

    def test_update_command(self):
        updated_data = {'name': 'UpdatedName'}
        response = self.client.put(reverse('command-detail', args=[self.command.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Update command should return 200 status code. Error: {response.content}')

    def test_delete_command(self):
        response = self.client.delete(reverse('command-detail', args=[self.command.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         msg=f'Delete command should return 204 status code. Error: {response.content}')


"""
Tests for Person.
"""


class PersonViewSetTestCase(APITestCase):
    def setUp(self):
        try:
            self.person_data_main = {'name': 'Monika', 'surname': 'Leblanc', 'mail': 'monikaL@example.com'}
            self.person = Person.objects.create(**self.person_data_main)
            self.url = 'http://127.0.0.1:8000/person/'
        except AssertionError as e:
            print(f'Test setUp for person failed: {str(e)}')

    def test_create_person(self):
        self.person_data = {'name': 'Chendler', 'surname': 'Bing', 'mail': 'chendlerB@example.com'}
        response = self.client.post(self.url, self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=f'Create command should return 201 status code. Error: {response.content}')

    def test_retrieve_person(self):
        response = self.client.get(reverse('person-detail', args=[self.person.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Retrieve command should return 200 status code. Error: {response.content}')

    def test_update_person(self):
        updated_data = {'name': 'UpdatedName', 'surname': self.person.surname, 'mail': self.person.mail}
        response = self.client.put(reverse('person-detail', args=[self.person.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg=f'Update command should return 200 status code. Error: {response.content}')

    def test_delete_person(self):
        response = self.client.delete(reverse('person-detail', args=[self.person.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         msg=f'Delete command should return 204 status code. Error: {response.content}')
