from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateViewSet.as_view()),
    path('delete', views.DeleteViewSet.as_view()),
    path('get_all_group', views.GetAllGroupViewSet.as_view()),
    path('add_contact_group', views.AddContactViewSet.as_view()),
    path('delete_contact_group', views.DeleteContactViewSet.as_view()),
]
