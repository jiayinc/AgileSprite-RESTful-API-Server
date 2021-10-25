from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginViewSet.as_view()),
    path('register', views.RegisterViewSet.as_view()),
    path('logout', views.LogOutViewSet.as_view()),
    path('update', views.UpdateViewSet.as_view()),
    path('get', views.GetViewSet.as_view()),
]
