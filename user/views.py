from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
# from django.shortcuts import render
from user.models import UserDetails
import json


# Create your views here.
def index(request):
    """

    """
    try:
        input_data = json.loads(request.body)
        print(input_data)
        print(request.method)
        return JsonResponse({"message": "you are at user index."})
    except Exception as e:
        print(e)


def registration(request):
    """
    creating the function named as registration
    :param request:
    :return:
    """
    try:
        input_data = json.loads(request.body)
        data = UserDetails.objects.create_user(username=input_data.get("username"), password=input_data.get("password"),
                                               email=input_data.get("email"),
                                               phone_number=input_data.get("phone_number"),
                                               location=input_data.get("location"))
        print(data)
        return JsonResponse({"message": "running fine"})
    except IntegrityError:
        exception = {'Exception': 'Already Exits...!'}
        return JsonResponse(exception)


def user_login(request):
    """
    create the user_login for getting into app
    """
    input_data = json.loads(request.body)
    try:

        if request.method == "POST":
            username = input_data.get('username')
            password = input_data.get('password')
            login_user = authenticate(username=username, password=password)
            if not login_user:
                data = {'message': 'please check your username and password'}
                return JsonResponse(data)
            return JsonResponse({'message': 'logged successfully'})
        return JsonResponse({'message': 'please check your request method'})
    except ValidationError:
        exception = {'Exception': " 'value doesn't Exits...!'"}
        return JsonResponse(exception)
