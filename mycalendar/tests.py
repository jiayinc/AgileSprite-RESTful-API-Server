import json
from django.urls import reverse
from common.code import *
from account.models import ExtendedUser as User
from rest_framework.test import APITestCase
from contact.models import Contact
from mycalendar.models import Event


class CalendarTests(APITestCase):
    def setUp(self):
       return

    def tearDown(self):
        return
        
    def test_create_event(self):
        Event.objects.create(date = "2021-11-11", user_id='1', name="peiyaa", category="peiyaa", start_time="2021-11-11 10:10:00", end_time="2021-11-11 10:10:00", comments="peiyaa", related_people="peiyaa")
        event_object = Event.objects.get(name="peiyaa")
        self.assertEqual(event_object.user_id, '1')

    def test_delete_event(self):
        Event.objects.create(date = "2021-11-11", user_id='1', name="peiyaa", category="peiyaa", start_time="2021-11-11 10:10", end_time="2021-11-11 10:10", comments="peiyaa", related_people="peiyaa")

        Event.objects.create(date = "2021-11-11", user_id='1', name="daniel", category="peiyaa", start_time="2021-11-11 10:10", end_time="2021-11-11 10:10", comments="peiyaa", related_people="peiyaa")
        event_list = Event.objects.all()
        self.assertEqual(event_list.count(), 2)
        Event.objects.get(name="daniel").delete()
        event_list = Event.objects.all()
        self.assertEqual(event_list.count(), 1)

    def test_update_event(self):
        Event.objects.create(date = "2021-11-11", user_id=1, name="peiyaa", category="peiyaa", start_time="2021-11-11 10:10", end_time="2021-11-11 10:10", comments="peiyaa", related_people="peiyaa")
        event = Event.objects.get(name="peiyaa")
        event.category = "peiyaa_2"
        event.save()
        self.assertEqual(Event.objects.get(name="peiyaa").category, "peiyaa_2")
    
    def test_get_day_event(self):
        Event.objects.create(date = "2021-11-11", user_id=1, name="daniel", category="peiyaa", start_time="2021-11-11 10:10", end_time="2021-11-11 10:10", comments="peiyaa", related_people="peiyaa")
        Event.objects.create(date = "2021-11-11", user_id=1, name="daniel2", category="peiyaa", start_time="2021-11-11 10:10", end_time="2021-11-11 10:10", comments="peiyaa", related_people="peiyaa")
        self.assertEqual(Event.objects.filter(date="2021-11-11").count(),2)
