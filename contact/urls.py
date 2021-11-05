from django.urls import path
from . import views

urlpatterns = [
    # add one contact
    path('add', views.AddViewSet.as_view(), name='contact-add'),
    # get all contacts
    path('get_all', views.GetAllViewSet.as_view(), name='contact-get_all'),
    # get a specific contact
    path('get', views.GetViewSet.as_view(), name='contact-get'),
    # delete a contact
    path('delete', views.DeleteViewSet.as_view(), name='contact-delete'),
    # update a contact
    path('update', views.UpdateViewSet.as_view(), name='contact-update'),
]
