from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.core import serializers
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Contact


def token_authentication(request):
    token = request.data.get('token')
    try:
        user_id = Token.objects.get(key=token).user_id
        return user_id
    except:
        return None


class AddViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = token_authentication(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})

        age = request.data.get('age')
        email = request.data.get('email')
        name = request.data.get('name')
        birthday = request.data.get('birthday')
        try:
            Contact.objects.create(age=age, email=email, name=name, user_id=user_id, birthday=birthday)
        except Exception as e:
            return JsonResponse({"code": 0,
                                 "msg": str(e)})

        return JsonResponse({"code": 0,
                             "msg": "add success"})


class GetAllViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = token_authentication(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        contacts = Contact.objects.filter(user_id=user_id)

        return JsonResponse({"code": 0,
                             "msg": "get success",
                             "contacts": list(contacts.values())})
