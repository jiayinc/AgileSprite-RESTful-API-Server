from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from common.common import get_user_id
from contact.models import Contact
from .models import Group
from .models import ContactGroup
from common.code import *
from django.core import serializers
import json


# Create your views here.
def token_authentication(request):
    token = request.data.get('token')
    try:
        user_id = Token.objects.get(key=token).user_id
        return user_id
    except:
        return None


class CreateViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0, "msg": "token authentication failed"})
        name = request.data.get('name')
        try:
            Group.objects.create(name=name, user_id=user_id)
        except Exception as e:
            return JsonResponse({"code": CREATE_GROUP_ERROR, "msg": str(e)})
        return JsonResponse({"code": CREATE_GROUP_SUCCESS, "msg": "create group success"})


class DeleteViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        group_id = request.data.get("id")
        try:
            Group.objects.filter(user_id=user_id, id=group_id).delete()
        except Exception as e:
            return JsonResponse({"code": DELETE_GROUP_ERROR, "msg": "delete group error"})
        return JsonResponse({"code": DELETE_GROUP_SUCCESS, "msg": "delete group sucess"})


class DeleteContactViewSet(APIView):
    def post(self, request, *arg, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        group_id = request.data.get("group_id")
        contact_id = request.data.get("contact_id")
        try:
            ContactGroup.objects.filter(contact_id=contact_id, group_id=group_id).delete()
        except Exception as e:
            return JsonResponse({"code": DELETE_CONTACT_ERROR, "msg": "delete contact error"})
        return JsonResponse({"code": DELETE_CONTACT_SUCCESS, "msg": "delete contact success"})


class AddContactViewSet(APIView):
    def post(self, request, *arg, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        group_id = request.data.get("group_id")
        contact_id = request.data.get("contact_id")
        try:
            ContactGroup.objects.create(contact_id=contact_id, group_id=group_id)
        except Exception as e:
            return JsonResponse({"code": ADD_CONTACT_ERROR, "msg": "add contact error"})
        return JsonResponse({"code": ADD_CONTACT_SUCCESS, "msg": "add contact success"})

class GetAllGroupViewSet(APIView):
    def post(self, request, *arg, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        try:
            group_list = serializers.serialize("json", Group.objects.all())
        except Exception as e:
            return JsonResponse({"code": ADD_CONTACT_ERROR, "msg": "add contact error"})
        print(json.dumps(group_list))
        return JsonResponse({"code": ADD_CONTACT_SUCCESS, "objects":  group_list})