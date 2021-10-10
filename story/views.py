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
