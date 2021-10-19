from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from contact.models import Contact
from common.code import *

def token_authentication(request):
    token = request.data.get('token')
    try:
        user_id = Token.objects.get(key=token).user_id
        return user_id
    except:
        return None

class ReminderBirthdayViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = token_authentication(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                 "msg": "token authentication failed"})
        date = request.data.get("date")
        contact_list = []
        try:
            contact_list = Contact.objects.filter(user_id=user_id, birthday=date)
        except Exception as e:
            return JsonResponse({"code":REMINDER_BIRTDAY_ERROR, "msg":"reminder birthday error"})
        return JsonResponse({"code":REMINDER_BIRTDAY_SUCCESS, "msg":contact_list})



class ViewStoryPhotoViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = token_authentication(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                 "msg": "token authentication failed"})
        date = request.data.get("date")
        contact_id = request.data.get("contact_id")
        story_list = []
        try:
            story_list = Story.objects.filter(contact_id=contact_id, date=date)
        except Exception as e:
            return JsonResponse({"code":VIEW_STORY_PHOTO_ERROR, "msg":"view story photo error"})
        return JsonResponse({"code":VIEW_STORY_PHOTO_SUCCESS, "msg":story_list})
