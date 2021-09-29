from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from .models import ExtendedUser as User

class LogOutViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        Token.objects.filter(key=token).delete()
        return JsonResponse({"code": 0,
                             "msg": "log out performed, token was disabled"})


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        # email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        dob = request.data.get('dob')
        try:
            user_id = Token.objects.get(key=token).user_id
        except:
            return JsonResponse({"code": 0,
                                "msg": "token error"})
        user_obj = User.objects.get(id=user_id)
        # user_obj.email = email
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.date_of_birth = dob
        try:
            user_obj.save()
        except Exception as e:
            return JsonResponse({"code": 0,
                                 "msg": str(e)})

        return JsonResponse({"code": 0,
                             "msg": "updated"})


class RegisterViewSet(APIView):

    def post(self, request, *args, **kwargs):
        # username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        try:
            User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
        except Exception as e:
            return JsonResponse({"code": 0,
                                 "msg": str(e)})
        return JsonResponse({"code": 0,
                             "msg": "create success"})


class LoginViewSet(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = auth.authenticate(username=email, password=password)
        if not user:
            return JsonResponse({"code": 0,
                                 "msg": "wrong username/password"})
        Token.objects.filter(user=user).delete()
        return JsonResponse({"code": 0,
                             "msg": "login success",
                             "token": Token.objects.create(user=user).key})
