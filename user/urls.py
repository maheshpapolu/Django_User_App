from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('user_login', views.user_login, name='user_login')

]
