from django.contrib.auth import authenticate
from django.db.migrations import serializer
from django.http import HttpResponse
import json
import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from user.models import UserDetails
from user.serializers import UserDetailsSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import EncodeDecodeToken
from django.core.mail import send_mail
from django.conf import settings

logging.basicConfig(filename='test.log', level=logging.ERROR)


class Registration(APIView):
    """
       List all user, or create a new user details.
    """

    @swagger_auto_schema(
        operation_summary="register",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='phone_number'),
            }
        ))
    def post(self, request):
        """

        """
        try:
            serializer = UserDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            encode_token = EncodeDecodeToken.encode_the_token(payload={'user_id': serializer.data.get('id')})
            send_mail(from_email=settings.EMAIL_HOST_USER, recipient_list=[serializer.data['email']],
                      message='welcome django_rest_framework, url is http://127.0.0.1:8000/user/validate/{}'.format(
                          encode_token),
                      subject='Link the registration', fail_silently=False, )
            logging.debug('registration done')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    @swagger_auto_schema(
        operation_summary="login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
            }
        ))
    def post(self, request):
        """
        create the user_login for getting into app
        """
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            login_user = authenticate(username=username, password=password)
            if login_user is not None:
                token = EncodeDecodeToken.encode_the_token(payload={'user_id': login_user.id})
                return Response({'message': 'successfully login', 'token': token},
                                status=status.HTTP_200_OK)
            return Response({'message': 'login failed'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ValidateToken(APIView):
    def get(self, request, token):
        try:
            decode_token = EncodeDecodeToken.decode_the_token(token)
            user = UserDetails.objects.get(id=decode_token.get('user_id'))
            user.is_verified = True
            user.save()
            return Response({'message': 'Validate successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return HttpResponse(e)
