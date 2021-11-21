import json
from django.urls import reverse
from common.code import *
from account.models import ExtendedUser as User
from rest_framework.test import APITestCase
from .models import Group
from .models import ContactGroup


class GroupTests(APITestCase):
    def setUp(self):
       return

    def tearDown(self):
        return
        
    def test_create_group(self):
        Group.objects.create(name="peiyaa", user_id="7")
        group = Group.objects.get(name="peiyaa")
        self.assertEqual(group.user_id, 7)

    def test_delete_group(self):
        Group.objects.create(name="daniel", user_id="1")
        Group.objects.create(name="peiyaa", user_id="7")

        group_list = Group.objects.all()
        self.assertEqual(group_list.count(), 2)
        Group.objects.get(name="daniel").delete()
        self.assertEqual(group_list.count(), 1)

    def test_add_contact(self):
        ContactGroup.objects.create(contact_id=1, group_id=2)
        contact_group = ContactGroup.objects.get(contact_id=1)
        self.assertEqual(contact_group.group_id, 2)

    def test_delete_contact(self):
        ContactGroup.objects.create(contact_id=3, group_id=4)
        contact_group_list = ContactGroup.objects.all()
        self.assertEqual(contact_group_list.count(), 1)
        ContactGroup.objects.get(contact_id = 3).delete()
        self.assertEqual(contact_group_list.count(), 0)

    def test_get_all_group(self):
        Group.objects.create(name="peiyaa", user_id="7")
        self.assertEqual(Group.objects.all().count(), 1)
