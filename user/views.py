import json
from django.http import JsonResponse
# from django.shortcuts import render
from user.models import UserDetails


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
        data = UserDetails.objects.create(username=input_data.get("username"), password=input_data.get("password"),
                                          email=input_data.get("email"), phone_number=input_data.get("phone_number"),
                                          location=input_data.get("location"))
        print(data)
        return JsonResponse({"message": "running fine"})
    except Exception as e:
        print(e)
        return JsonResponse({"message": "error"})


def user_login(request):
    """
    create the user_login for getting into app
    """
    try:
        input_data = json.loads(request.body)
        if request.method == "POST":
            username = input_data.get('username')
            password = input_data.get('password')
            login_user = UserDetails.objects.filter(username=username, password=password)
            if not login_user:
                data = {'message': 'please check your username and password'}
                return JsonResponse(data)
            else:
                return JsonResponse({'message': 'correct data entered'})
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'error in your program'})
