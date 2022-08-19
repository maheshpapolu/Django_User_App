from django.contrib.auth import authenticate
# from django.http import JsonResponse
# from user.models import UserDetails
# import json
import logging
# from user.models import UserDetails
from user.serializers import UserDetailsSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logging.basicConfig(filename='test.log', level=logging.ERROR)


class Registration(APIView):
    """
       List all user, or create a new user details.
    """

    def post(self, request):
        """

        """
        try:
            serializer = UserDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):

    def post(self, request):
        """
        create the user_login for getting into app
        """
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            login_user = authenticate(username=username, password=password)
            if login_user is not None:
                return Response({'message': 'successfully login'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
