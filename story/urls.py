from django.urls import path
from . import views

urlpatterns = [
    # get a story by applying filters
    path('get', views.GetViewSet.as_view(), name='story-get'),
    # get all stories
    path('get_all', views.GetAllViewSet.as_view(), name='story-get_all'),
    # add a story
    path('add', views.AddViewSet.as_view(), name='story-add'),
    # delete a story
    path('delete', views.GetAllViewSet.as_view(), name='story-delete'),
    # update a story
    path('update', views.UpdateViewSet.as_view(), name='story-update'),
]

