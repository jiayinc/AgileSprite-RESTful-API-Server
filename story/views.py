from common.code import *
from common.common import get_user_id
from .models import Story
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.
class GetAllViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})
        contact_id = request.data.get('contact_id')
        stories = Story.objects.filter(contact_id=contact_id, user_id=user_id)

        return JsonResponse({"code": STORY_GET_ALL_SUCCESS,
                             "msg": "get success",
                             "Stories": list(stories.values())})

class AddViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        contact_id = request.data.get('contact_id')
        location = request.data.get('location')
        date = request.data.get('date')
        content = request.data.get('content')
        try:
            if contact_id is None:
                raise Exception("no contact id provided")
            Story.objects.create(contact_id=contact_id,
                                 location=location,
                                 date=date,
                                 content=content,
                                 user_id=user_id)
        except Exception as e:
            return JsonResponse({"code": STORY_ADD_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": STORY_ADD_SUCCESS,
                             "msg": "add success"})

class GetViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        story_id = request.data.get('story_id')
        contact_id = request.data.get('contact_id')
        stories = Story.objects.filter(contact_id=contact_id, id=story_id, user_id=user_id)

        return JsonResponse({"code": STORY_GET_SUCCESS,
                             "msg": "get success",
                             "Stories": list(stories.values())})


class DeleteViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})
        story_id = request.data.get('story_id')
        contact_id = request.data.get('contact_id')
        Story.objects.filter(user_id=user_id, id=story_id, contact_id=contact_id).delete()

        return JsonResponse({"code": STORY_DELETE_SUCCESS,
                             "msg": "delete success"})


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        location = request.data.get('location')
        date = request.data.get('date')
        content = request.data.get('content')
        try:
            contact_id = request.data.get('contact_id')
            story_id = request.data.get('story_id')
            story = Story.objects.get(id=story_id, user_id=user_id, contact_id=contact_id)
        except:
            return JsonResponse({"code": STORY_ID_NOT_EXIST,
                                 "msg": "contact ID does not exist"})

        if location is not None:
            story.location = location
        if date is not None:
            story.date = date
        if content is not None:
            story.content = content

        try:
            story.save()
        except Exception as e:
            return JsonResponse({"code": STORY_UPDATE_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": STORY_UPDATE_SUCCESS,
                             "msg": "updated"})
