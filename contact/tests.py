import json
from django.urls import reverse
from common.code import *
from account.models import ExtendedUser as User
from rest_framework.test import APITestCase


class ContactCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-add')
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
            'first_name': 'test'
        }
        self.code = CONTACT_ADD_FAIL

    def test_wrong_3(self):
        self.data = {
            'token': self.token,
            'last_name': 'test_last'
        }
        self.code = CONTACT_ADD_FAIL

    def test_correct_1(self):
        self.data = {
            'token': self.token,
            'last_name': 'test_last',
            'first_name': 'test'
        }
        self.code = CONTACT_ADD_SUCCESS


class ContactDeleteTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-delete')
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


class ContactGetAllTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-get_all')
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


class ContactGetTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-get')
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


class ContactUpdateTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-update')
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
