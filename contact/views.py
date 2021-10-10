# Create your views here.

from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Contact
from common.common import get_user_id


class AddViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})

        email = request.data.get('email')
        name = request.data.get('name')
        birthday = request.data.get('birthday')
        try:
            Contact.objects.create(email=email, name=name, user_id=user_id, birthday=birthday)
        except Exception as e:
            return JsonResponse({"code": 0,
                                 "msg": str(e)})

        return JsonResponse({"code": 0,
                             "msg": "add success"})


class GetAllViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})
        contacts = Contact.objects.filter(user_id=user_id)

        return JsonResponse({"code": 0,
                             "msg": "get success",
                             "contacts": list(contacts.values())})


class GetViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})

        contact_id = request.data.get('contact_id')
        contacts = Contact.objects.filter(user_id=user_id, id=contact_id)

        return JsonResponse({"code": 0,
                             "msg": "get success",
                             "contacts": list(contacts.values())})


class DeleteViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})

        contact_id = request.data.get('contact_id')
        Contact.objects.filter(user_id=user_id, id=contact_id).delete()

        return JsonResponse({"code": 0,
                             "msg": "delete success"})


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": 0,
                                 "msg": "token authentication failed"})

        name = request.data.get('name')
        company = request.data.get('company')
        email = request.data.get('email')
        phone = request.data.get('phone')
        mobile = request.data.get('mobile')
        address = request.data.get('address')
        birthday = request.data.get('birthday')
        relationship = request.data.get('relationship')
        notes = request.data.get('notes')
        image_address = request.data.get('image_address')
        contact_id = request.data.get('contact_id')
        contacts = Contact.objects.get(id=contact_id)

        contacts.name = name
        contacts.company = company
        contacts.email = email
        contacts.phone = phone
        contacts.mobile = mobile
        contacts.address = address
        contacts.birthday = birthday
        contacts.relationship = relationship
        contacts.notes = notes
        contacts.image_address = image_address

        try:
            contacts.save()
        except Exception as e:
            return JsonResponse({"code": 0,
                                 "msg": str(e)})

        return JsonResponse({"code": 0,
                             "msg": "updated"})
