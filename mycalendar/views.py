from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from contact.models import Contact
from mycalendar.models import Event
from common.common import get_user_id
from common.code import *
from django.core import serializers


class ReminderBirthdayViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                 "msg": "token authentication failed"})
        date = request.data.get("date")
        contact_list = []
        try:
            contact_list = Contact.objects.filter(user_id=user_id, birthday=date)
        except Exception as e:
            return JsonResponse({"code":REMINDER_BIRTDAY_ERROR, "msg":"reminder birthday error"})
        return JsonResponse({"code":REMINDER_BIRTDAY_SUCCESS, "objects":contact_list})


class ViewStoryPhotoViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
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
        return JsonResponse({"code":VIEW_STORY_PHOTO_SUCCESS, "objects":story_list})

class CreateEventViewSet(APIView):
    def post(self, request, *args, **kwars):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                "msg": "token authentication failed"})
        location = request.data.get("location")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        related_people = request.data.get("related_people")
        comment = request.data.get("comment")
        name = request.data.get("name")
        category = request.data.get("category")
        date = request.data.get("date")
        print(date + location + start_time + end_time + name + category + related_people + comment)
        try:
            Event.objects.create(date = date, user_id=user_id, name=name, category=category, start_time=start_time, end_time=end_time, comments=comment, related_people=related_people)
        except Exception as e:
            return JsonResponse({"code":CREATE_EVENT_ERROR, "msg":"create event failed" + str(e)})
        return JsonResponse({"code":CREATE_EVENT_SUCCESS, "msg":"create event successfuly"})
class UpdateEventViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                "msg": "token authentication failed"})     
        id = request.data.get("id")
        try:
            event = Event.objects.get(id = id)
        except Exception as e:
            return JsonResponse({"code":0, "msg":"get event failed " + str(e)})

        location = request.data.get("location")
        if location is not None:
            event.location = location
        
        start_time = request.data.get("start_time")
        if start_time is not None:
            event.start_time = start_time
        end_time = request.data.get("end_time")
        if end_time is not None:
            event.end_time = end_time
        related_people = request.data.get("related_people")
        if related_people is not None:
            event.related_people = related_people
        comment = request.data.get("comment")
        if comment is not None:
            event.comments = comment
        name = request.data.get("name")
        if name is not None:
            event.name = name
        category = request.data.get("category")
        if category is not None:
            event.category = category

        try:
           event.save()
        except Exception as e:
            return JsonResponse({"code":UPDATE_EVENT_ERROR, "msg":"save event failed"})
        return JsonResponse({"code":UPDATE_EVENT_SUCCESS, "msg":"update event successfuly"}) 
class DeleteEventViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code":0,
                                "msg":"token authentication failed"})
                            
        id = request.data.get("id")
        try:
            Event.objects.filter(id = id).delete()
        except Exception as e:
            return JsonResponse({"code":DELETE_EVENT_ERROR, "msg":"delete event failed"})
        return JsonResponse({"code":DELETE_EVENT_SUCC, "msg":"delete event succ"})
class GetDayEventsViewSet(APIView):
    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code":0, 
                                "msg":"token authentication failed"})
        date = request.data.get("date")
        try:
            event_list = serializers.serialize("json", Event.objects.filter(date = date, user_id = user_id))
        except Exception as e:
            return JsonResponse({"code":GET_EVENT_ERROR, "msg":"get event failed"})
        return JsonResponse({"code":GET_EVENT_SUCC,"jobects": event_list})
