from django.urls import path
from user import views

urlpatterns = [
    path('Registration', views.Registration.as_view(), name='Registration'),
    path('Login', views.Login.as_view(), name='Login'),
]
