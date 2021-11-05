from django.urls import path
from . import views

urlpatterns = [
    # get all stories
    path('get_all', views.GetAllViewSet.as_view()),
    # get a story by applying filters
    path('get', views.GetViewSet.as_view()),
    # get all stories
    path('get_all', views.GetAllViewSet.as_view()),
    # add a story
    path('add', views.AddViewSet.as_view()),
    # delete a story
    path('delete', views.GetAllViewSet.as_view()),
    # update a story
    path('update', views.UpdateViewSet.as_view()),
]

