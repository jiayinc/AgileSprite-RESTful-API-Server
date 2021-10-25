from django.urls import path
from . import views

urlpatterns = [
    # get total number of stories
    path('get_count', views.GetAllViewSet.as_view()),
    # get story(s) by applying filters
    # path('story/get', views.GetAllViewSet.as_view()),
    # get all stories
    path('get_all', views.GetAllViewSet.as_view()),
    # add a story
    path('add', views.AddViewSet.as_view()),
    # delete a story
    path('delete', views.GetAllViewSet.as_view()),
]

