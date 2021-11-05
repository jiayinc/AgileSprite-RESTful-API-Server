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

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        # no password field
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_REGISTER_PASSWORD_INVALID

    def test_wrong_2(self):
        # no lowercase
        self.data = {
            'password': '123456ASD'
        }
        self.code = ACCOUNT_REGISTER_PASSWORD_INVALID

    def test_wrong_3(self):
        # no uppercase
        self.data = {
            'password': '123456ab'
        }
        self.code = ACCOUNT_REGISTER_PASSWORD_INVALID

    def test_wrong_4(self):
        # long password
        self.data = {
            'password': '123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab123ASDab',
        }
        self.code = ACCOUNT_REGISTER_PASSWORD_INVALID

    def test_wrong_5(self):
        # correct password, but no email field
        self.data = {
            'password': '123ASDab123A',
        }
        self.code = ACCOUNT_REGISTER_EMAIL_INVALID

    def test_wrong_6(self):
        # correct password
        # email wrong format
        self.data = {
            'password': '123ASDab123A',
            'email': 'abxxxc'
        }
        self.code = ACCOUNT_REGISTER_EMAIL_INVALID

    def test_wrong_7(self):
        # correct password
        # email wrong format
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@'
        }
        self.code = ACCOUNT_REGISTER_EMAIL_INVALID

    def test_wrong_8(self):
        # correct password
        # email wrong format
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@qq'
        }
        self.code = ACCOUNT_REGISTER_EMAIL_INVALID

    def test_wrong_9(self):
        # correct password
        # correct email
        # no names
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com'
        }
        self.code = ACCOUNT_REGISTER_ERROR

    def test_wrong_10(self):
        # correct password
        # correct email
        # no last name
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'first_name': 'test'
        }
        self.code = ACCOUNT_REGISTER_ERROR

    def test_wrong_11(self):
        # correct password
        # correct email
        # no first name
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'last_name': 'gg'
        }
        self.code = ACCOUNT_REGISTER_ERROR

    def test_correct_1(self):
        # correct password
        # correct email
        # correct name
        self.data = {
            'password': '123ASDab123A',
            'email': 'abc@qq11.com',
            'first_name': 'test',
            'last_name': 'gg'
        }
        self.code = ACCOUNT_REGISTER_SUCCESS


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

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        # no login details
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_LOGIN_EMAIL_INVALID

    def test_wrong_2(self):
        # no password
        self.data = {
            'email': 'email@email.co'
        }
        self.code = ACCOUNT_LOGIN_PASSWORD_INVALID

    def test_wrong_3(self):
        # email wrong
        self.data = {
            'email': 'email@email.co',
            'password': 'passwordASD123'
        }
        self.code = ACCOUNT_LOGIN_FAIL

    def test_wrong_4(self):
        # password wrong
        self.data = {
            'email': 'email@email.com',
            'password': 'passwordASD'
        }
        self.code = ACCOUNT_LOGIN_PASSWORD_INVALID

    def test_correct_1(self):
        # correct credentials
        self.data = {
            'email': 'email@email.com',
            'password': 'passwordASD123'
        }
        self.code = ACCOUNT_LOGIN_SUCCESS


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

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)

    def test_wrong_1(self):
        # no token
        self.data = {
            'random': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR

    def test_wrong_2(self):
        # wrong token
        self.data = {
            'token': '123'
        }
        self.code = ACCOUNT_TOKEN_ERROR

    def test_correct_1(self):
        # correct token
        self.data = {
            'token': self.token
        }
        self.code = ACCOUNT_LOGOUT_SUCCESS


class AccountGetTests(APITestCase):

    def setUp(self):
        self.url = reverse('account-get')
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

        self.first_name = None
        self.last_name = None

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)
        if self.first_name:
            self.assertEqual(content['details']['first_name'], self.first_name)
            self.first_name = None
        if self.last_name:
            self.assertEqual(content['details']['last_name'], self.last_name)
            self.last_name = None

    def test_correct_1(self):
        # correct token
        self.data = {
            'token': self.token
        }
        self.code = ACCOUNT_GET_SUCCESS
        self.first_name = 'first'
        self.last_name = 'last'

    def test_wrong_1(self):
        # wrong token
        self.data = {
            'token': 'abc'
        }
        self.code = ACCOUNT_TOKEN_ERROR
