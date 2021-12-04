import json
from django.urls import reverse
from common.code import *
from account.models import ExtendedUser as User
from rest_framework.test import APITestCase


class StoryCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('story-add')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR

    def test_wrong_2(self):
        self.data = {
            'token': self.token,
            'contact_id': 99
        }
        self.code = STORY_ADD_FAIL

    def test_wrong_3(self):
        self.data = {
            'token': self.token,
            'location': 'test_last'
        }
        self.code = STORY_ADD_FAIL

    def test_correct_1(self):
        self.data = {
            'token': self.token,
            'contact_id': 3,
            'location': 'mel',
            'content': 'what???',
            'date': '2020-01-21'
        }
        self.code = STORY_ADD_SUCCESS


class StoryDeleteTests(APITestCase):
    def setUp(self):
        self.url = reverse('story-delete')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR


class StoryGetAllTests(APITestCase):
    def setUp(self):
        self.url = reverse('story-get_all')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR


class StoryGetTests(APITestCase):
    def setUp(self):
        self.url = reverse('story-get')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR


class StoryUpdateTests(APITestCase):
    def setUp(self):
        self.url = reverse('story-update')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR
