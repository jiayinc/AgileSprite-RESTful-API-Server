from django.urls import path
from . import views

urlpatterns = [
    path('reminder_birthday', views.ReminderBirthdayViewSet.as_view()),
    path('view_story_photo', views.ViewStoryPhotoViewSet.as_view()),
    path('create_event', views.CreateEventViewSet.as_view()),
    path('update_event', views.UpdateEventViewSet.as_view()),
    path('delete_event', views.DeleteEventViewSet.as_view()),
    path('get_day_events', views.GetDayEventsViewSet.as_view()),
]
