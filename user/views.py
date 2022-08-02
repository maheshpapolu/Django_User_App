from django.contrib.auth import authenticate
from django.http import JsonResponse
from user.models import UserDetails
import json
import logging

logging.basicConfig(filename='test.log', level=logging.ERROR)


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
        logging.error("raised the error in code", exc_info=True)
        return JsonResponse({'message': 'error in our code'})


def registration(request):
    """
    creating the function named as registration
    :param request:
    :return:
    """
    try:
        input_data = json.loads(request.body)
        print(input_data)
        data = UserDetails.objects.create_user(username=input_data.get("username"), password=input_data.get("password"),
                                               email=input_data.get("email"), phone_number=input_data.get('phone_number'),
                                               location=input_data.get('location'))
        return JsonResponse({"message": "running fine"})
    except Exception as e:
        logging.error(e)
        return JsonResponse({'message': 'error in our code'})


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
            print(login_user)
            if login_user is not None:
                data = {'message': 'logged successfully'}
                return JsonResponse(data)
            return JsonResponse({'message': 'check the username and password'})
        return JsonResponse({'message': 'please check your request method'})
    except Exception as e:
        logging.error(e)
        return JsonResponse({'message': 'error in our code'})
