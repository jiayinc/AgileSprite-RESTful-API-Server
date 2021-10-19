from django.urls import path
from . import views

urlpatterns = [
    path('reminder_birthday', views.ReminderBirthdayViewSet.as_view()),
    path('view_story_photo', views.ViewStoryPhotoViewSet.as_view()),
]
