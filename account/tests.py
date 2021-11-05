import json
from django.urls import reverse
from common.code import *
from .models import ExtendedUser as User
from rest_framework.test import APITestCase


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

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)
        if self.code == ACCOUNT_GET_SUCCESS:
            self.assertEqual(content['details']['first_name'], self.user.first_name)
            self.assertEqual(content['details']['last_name'], self.user.last_name)
            self.assertEqual(content['details']['email'], self.user.email)

    def test_correct_1(self):
        # correct token
        self.data = {
            'token': self.token
        }
        self.code = ACCOUNT_GET_SUCCESS

    def test_wrong_1(self):
        # wrong token
        self.data = {
            'token': 'abc'
        }
        self.code = ACCOUNT_TOKEN_ERROR


class AccountUpdateTests(APITestCase):

    # no content validation still

    def setUp(self):
        self.url = reverse('account-update')
        self.user = User.objects.create_user(username='email@email.com',
                                             password='passwordASD123',
                                             email='email@email.com',
                                             first_name='first',
                                             last_name='last')
        data = {
            'email': self.user.email,
            'password': 'passwordASD123'
        }
        response = self.client.post(reverse('account-login'), data, format='json')
        content = json.loads(response.content)
        self.token = content['token']
        self.new_email = None
        self.new_first_name = None
        self.new_last_name = None

    def tearDown(self):
        response = self.client.post(self.url, self.data, format='json')
        content = json.loads(response.content)
        self.assertEqual(content['code'], self.code)
        if self.code == ACCOUNT_UPDATE_SUCCESS:
            if self.new_email:
                self.user_test = User.objects.get(username=self.new_email)
            else:
                self.user_test = User.objects.get(username=self.user.email)

            if self.new_first_name:
                self.assertEqual(self.new_first_name, self.user_test.first_name)

            if self.new_last_name:
                self.assertEqual(self.new_last_name, self.user_test.last_name)

    def test_wrong_1(self):
        # wrong token
        # nothing to update
        self.data = {
            'token': 'abc'
        }
        self.code = ACCOUNT_TOKEN_ERROR

    def test_wrong_2(self):
        # wrong token
        # nothing to update
        self.data = {
            'token': 'abc',
            'first_name': 'name'
        }
        self.code = ACCOUNT_TOKEN_ERROR

    def test_correct_1(self):
        # correct token
        # nothing to update
        self.data = {
            'token': self.token
        }
        self.code = ACCOUNT_UPDATE_SUCCESS

    def test_correct_2(self):
        # correct token
        # update all
        self.new_first_name = 'a'
        self.new_last_name = 'b'
        self.new_email = 'email@qq.com'
        self.data = {
            'token': self.token,
            'first_name': self.new_first_name,
            'last_name': self.new_last_name,
            'email': self.new_email,
        }
        self.code = ACCOUNT_UPDATE_SUCCESS

    def test_wrong_3(self):
        # correct token
        # wrong email format
        self.data = {
            'token': self.token,
            'email': 'email',
        }
        self.code = ACCOUNT_UPDATE_EMAIL_INVALID

    def test_wrong_4(self):
        # correct token
        # wrong email format
        self.data = {
            'token': self.token,
            'email': 'email@qx',
        }
        self.code = ACCOUNT_UPDATE_EMAIL_INVALID

    def test_wrong_5(self):
        # correct token
        # wrong email format
        self.data = {
            'token': self.token,
            'email': 'email@.com',
        }
        self.code = ACCOUNT_UPDATE_EMAIL_INVALID

    def test_wrong_6(self):
        # correct token
        # wrong password format
        self.data = {
            'token': self.token,
            'password': 'abc',
        }
        self.code = ACCOUNT_UPDATE_PASSWORD_INVALID

    def test_wrong_7(self):
        # correct token
        # wrong password format
        self.data = {
            'token': self.token,
            'password': 'abcABC1',
        }
        self.code = ACCOUNT_UPDATE_PASSWORD_INVALID

    def test_wrong_8(self):
        # correct token
        # wrong password format
        self.data = {
            'token': self.token,
            'password': 'abcd1234',
        }
        self.code = ACCOUNT_UPDATE_PASSWORD_INVALID

    def test_wrong_9(self):
        # correct token
        # wrong password format
        self.data = {
            'token': self.token,
            'password': 'abcd123abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234ab4',
        }
        self.code = ACCOUNT_UPDATE_PASSWORD_INVALID

    def test_correct_3(self):
        # correct token
        # correct password format
        self.data = {
            'token': self.token,
            'password': 'abcABC123',
        }
        self.code = ACCOUNT_UPDATE_SUCCESS

    def test_wrong_10(self):
        # correct token
        # email exists
        self.data = {
            'token': self.token,
            'email': 'email@exist.com',
        }
        User.objects.create_user(username='email@exist.com',
                                 password='passwordASD123',
                                 email='email@exist.com',
                                 first_name='first',
                                 last_name='last')
        self.code = ACCOUNT_UPDATE_EMAIL_INVALID
