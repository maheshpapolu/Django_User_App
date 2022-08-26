from django.urls import path
from user import views

urlpatterns = [
    path('Registration', views.Registration.as_view(), name='Registration'),
    path('login', views.Login.as_view(), name='login'),
    path('validate/<str:token>', views.ValidateToken.as_view(), name='validate')
]
