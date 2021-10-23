from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from .models import ExtendedUser as User
from common.code import *


class LogOutViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        try:
            Token.objects.get(key=token).delete()
            return JsonResponse({"code": ACCOUNT_LOGOUT_SUCCESS,
                                 "msg": "log out performed, token was disabled"})
        except:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token does not exist"})
        # Token.objects.filter(key=token).delete()


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        # email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        dob = request.data.get('dob')
        password = request.data.get('password')
        email = request.data.get('email')
        try:
            user_id = Token.objects.get(key=token).user_id
        except:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token error"})
        user_obj = User.objects.get(id=user_id)
        # user_obj.email = email
        if first_name is not None:
            user_obj.first_name = first_name
        if last_name is not None:
            user_obj.last_name = last_name
        if dob is not None:
            user_obj.date_of_birth = dob
        if password is not None:
            user_obj.password = password
        if email is not None:
            user_obj.email = email
            user_obj.username = email
        try:
            user_obj.save()
        except Exception as e:
            return JsonResponse({"code": ACCOUNT_UPDATE_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": ACCOUNT_UPDATE_SUCCESS,
                             "msg": "updated"})


class InvalidPassword(Exception):
    message = "Password must contains at least a digit, a letter, a upper case letter and a symbol, " \
              "and length is between 8 and 30"

    def __str__(self):
        return self.message


class RegisterViewSet(APIView):

    def validate_password(self, password):
        import re
        reg = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,30}$'
        if re.match(reg, password):
            return True
        else:
            raise InvalidPassword

    def post(self, request, *args, **kwargs):
        # username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        try:
            self.validate_password(password)
            User.objects.create_user(username=email, password=password, email=email, first_name=first_name,
                                     last_name=last_name)
        except InvalidPassword as e:
            return JsonResponse({"code": ACCOUNT_REGISTER_PASSWORD_INVALID,
                                 "msg": str(e)})
        except Exception as e:
            if "account_extendeduser.username" in str(e):
                return JsonResponse({"code": ACCOUNT_REGISTER_REPEAT_EMAIL,
                                     "msg": "This email address has been registered, a different email address is "
                                            "required for sign up."})
            else:
                # Other unexpected errors occurred
                return JsonResponse({"code": ACCOUNT_REGISTER_ERROR,
                                     "msg": "Unexpected errors occurred!"})

        return JsonResponse({"code": ACCOUNT_REGISTER_SUCCESS,
                             "msg": "create success"})


class LoginViewSet(APIView):

    def validate_user(self, request):
        pass

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None:
            return JsonResponse({"code": ACCOUNT_LOGIN_EMPTY_EMAIL,
                                 "msg": "email is empty"})

        if password is None:
            return JsonResponse({"code": ACCOUNT_LOGIN_EMPTY_PASSWORD,
                                 "msg": "password is empty"})

        user = auth.authenticate(username=email, password=password)
        if not user:
            return JsonResponse({"code": ACCOUNT_LOGIN_FAIL,
                                 "msg": "wrong email/password"})
        Token.objects.filter(user=user).delete()
        return JsonResponse({"code": ACCOUNT_LOGIN_SUCCESS,
                             "msg": "login success",
                             "token": Token.objects.create(user=user).key})
