import json

from django.urls import reverse
from rest_framework import status
from common.code import *
from .models import ExtendedUser as User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class AccountCreateTests(APITestCase):
    def setUp(self):
        self.url = reverse('account-register')

    def test_wrong_1(self):
        # no password field
        data = {
            'random': '123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_PASSWORD_INVALID)

    def test_wrong_2(self):
        # no lowercase
        data = {
            'password': '123456ASD'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_PASSWORD_INVALID)

    def test_wrong_3(self):
        # no uppercase
        data = {
            'password': '123456ab'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_PASSWORD_INVALID)

    def test_wrong_4(self):
        # long password
        data = {
            'password': '123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab',
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_PASSWORD_INVALID)

    def test_wrong_5(self):
        # correct password, but no email field
        data = {
            'password': '123ASDab123A',
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_EMAIL_INVALID)

    def test_wrong_6(self):
        # correct password
        # email wrong format
        data = {
            'password': '123ASDab123A',
            'email': 'abxxxc'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_EMAIL_INVALID)

    def test_wrong_7(self):
        # correct password
        # email wrong format
        data = {
            'password': '123ASDab123A',
            'email': 'abc@'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_EMAIL_INVALID)

    def test_wrong_8(self):
        # correct password
        # email wrong format
        data = {
            'password': '123ASDab123A',
            'email': 'abc@qq'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_EMAIL_INVALID)

    def test_wrong_9(self):
        # correct password
        # correct email
        # no names
        data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_ERROR)

    def test_wrong_10(self):
        # correct password
        # correct email
        # no last name
        data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'first_name': 'test'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_ERROR)

    def test_wrong_11(self):
        # correct password
        # correct email
        # no first name
        data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'last_name': 'gg'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_ERROR)

    def test_correct_1(self):
        # correct password
        # correct email
        # correct name
        data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'first_name': 'test',
            'last_name': 'gg'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_REGISTER_SUCCESS)


class AccountLoginTests(APITestCase):

    def setUp(self):
        self.url = reverse('account-login')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        # self.client = APIClient()
        # self.client.force_authenticate(self.user)

    def test_wrong_1(self):
        # no login details
        data = {
            'random': '123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGIN_EMAIL_INVALID)

    def test_wrong_2(self):
        # no password
        data = {
            'email': 'email@email.co'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGIN_PASSWORD_INVALID)

    def test_wrong_3(self):
        # email wrong
        data = {
            'email': 'email@email.co',
            'password': 'passwordASD123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGIN_FAIL)

    def test_wrong_4(self):
        # password wrong
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGIN_PASSWORD_INVALID)

    def test_correct_1(self):
        # correct credentials
        data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGIN_SUCCESS)

class AccountLogoutTests(APITestCase):

    def setUp(self):
        self.url = reverse('account-logout')
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

    def test_wrong_1(self):
        # no token
        data = {
            'random': '123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_TOKEN_ERROR)

    def test_wrong_2(self):
        # wrong token
        data = {
            'token': '123'
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_TOKEN_ERROR)

    def test_correct_1(self):
        # wrong token
        data = {
            'token': self.token
        }
        response = self.client.post(self.url, data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], ACCOUNT_LOGOUT_SUCCESS)
