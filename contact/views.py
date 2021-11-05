# Create your views here.

from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Contact
from common.common import get_user_id
from common.code import *


class AddViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        # email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        try:
            contact = Contact.objects.create(first_name=first_name, last_name=last_name, user_id=user_id)
        except Exception as e:
            return JsonResponse({"code": CONTACT_ADD_FAIL,
                                 "msg": str(e)})

        company = request.data.get('company')
        email = request.data.get('email')
        phone = request.data.get('phone')
        mobile = request.data.get('mobile')
        address = request.data.get('address')
        birthday = request.data.get('birthday')
        relationship = request.data.get('relationship')
        notes = request.data.get('notes')
        image_address = request.data.get('image_address')

        is_not_empty = lambda x: x is not None and len(x) != 0

        contact.company = company if is_not_empty(company) else ''
        contact.email = email if is_not_empty(email) else ''
        contact.phone = phone if is_not_empty(phone) else ''
        contact.mobile = mobile if is_not_empty(mobile) else ''
        contact.address = address if is_not_empty(address) else ''
        contact.birthday = birthday if is_not_empty(birthday) else "1970-01-01"
        contact.relationship = relationship if is_not_empty(relationship) else ''
        contact.notes = notes if is_not_empty(notes) else ''
        contact.image_address = image_address if is_not_empty(image_address) else ("https://i.pravatar.cc/150?u=" + first_name + last_name + str(contact.id))
        try:
            contact.save()
        except Exception as e:
            return JsonResponse({"code": CONTACT_ADD_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": CONTACT_ADD_SUCCESS,
                             "msg": "add success"
                             })


class GetAllViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})
        contacts = Contact.objects.filter(user_id=user_id)

        return JsonResponse({"code": CONTACT_GET_ALL_SUCCESS,
                             "msg": "get success",
                             "contacts": list(contacts.values())})


class GetViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        contact_id = request.data.get('contact_id')
        contacts = Contact.objects.filter(user_id=user_id, id=contact_id)

        return JsonResponse({"code": CONTACT_GET_SUCCESS,
                             "msg": "get success",
                             "contacts": list(contacts.values())})


class DeleteViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        contact_id = request.data.get('contact_id')
        Contact.objects.filter(user_id=user_id, id=contact_id).delete()

        return JsonResponse({"code": CONTACT_DELETE_SUCCESS,
                             "msg": "delete success"})


class UpdateViewSet(APIView):

    def post(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        if user_id is None:
            return JsonResponse({"code": ACCOUNT_TOKEN_ERROR,
                                 "msg": "token authentication failed"})

        # name = request.data.get('name')
        company = request.data.get('company')
        email = request.data.get('email')
        phone = request.data.get('phone')
        mobile = request.data.get('mobile')
        address = request.data.get('address')
        birthday = request.data.get('birthday')
        relationship = request.data.get('relationship')
        notes = request.data.get('notes')
        image_address = request.data.get('image_address')
        try:
            contact_id = request.data.get('contact_id')
            contacts = Contact.objects.get(id=contact_id, user_id=user_id)
        except:
            return JsonResponse({"code": CONTACT_ID_NOT_EXIST,
                                 "msg": "contact ID does not exist"})

        # if name is not None:
        #     contacts.name = name
        if company is not None:
            contacts.company = company
        if email is not None:
            contacts.email = email
        if phone is not None:
            contacts.phone = phone
        if mobile is not None:
            contacts.mobile = mobile
        if address is not None:
            contacts.address = address
        if birthday is not None and len(birthday) != 0:
            contacts.birthday = birthday
        if relationship is not None:
            contacts.relationship = relationship
        if notes is not None:
            contacts.notes = notes
        if image_address is not None:
            contacts.image_address = image_address

        try:
            contacts.save()
        except Exception as e:
            return JsonResponse({"code": CONTACT_UPDATE_FAIL,
                                 "msg": str(e)})

        return JsonResponse({"code": CONTACT_UPDATE_SUCCESS,
                             "msg": "updated"})
