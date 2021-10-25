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
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        stories = Story.objects.filter(user_id=user_id)

        return JsonResponse({"code": 0,
                             "msg": "get success",
                             "contacts": list(stories.values())})

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
            Story.objects.create(contact_id=contact_id, location=location, date=date, content=content)
        except Exception as e:
            return JsonResponse({"code": STORY_ADD_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": STORY_ADD_SUCCESS,
                             "msg": "add success"})
