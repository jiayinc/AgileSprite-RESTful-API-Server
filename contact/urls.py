from django.urls import path
from . import views

urlpatterns = [
    path('add', views.AddViewSet.as_view()),
    path('get_all', views.GetAllViewSet.as_view()),
]
