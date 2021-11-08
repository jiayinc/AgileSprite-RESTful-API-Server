from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginViewSet.as_view(), name='account-login'),
    path('register', views.RegisterViewSet.as_view(), name='account-register'),
    path('logout', views.LogOutViewSet.as_view(), name='account-logout'),
    path('update', views.UpdateViewSet.as_view(), name='account-update'),
    path('get', views.GetViewSet.as_view(), name='account-get'),
    path('forgotpassword', views.ForgotPasswordViewSet.as_view(), name='account-forgotpassword'),
]
