from django.urls import path
from . import views

urlpatterns = [
    # add one contact
    path('add', views.AddViewSet.as_view()),
    # get all contacts
    path('get_all', views.GetAllViewSet.as_view()),
    # get a specific contact
    path('get', views.GetViewSet.as_view()),
    # delete a contact
    path('delete', views.DeleteViewSet.as_view()),
    # update a contact
    path('update', views.UpdateViewSet.as_view()),
]
