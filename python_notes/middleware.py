from user.models import LogTable
import logging

logging.basicConfig(level=logging.INFO, filename='abc.log')


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Welcome")

        response = self.get_response(request)
        self.log_api(request)

        return response

    def log_api(self, request):
        log = LogTable(type_of_request=request.method, response=request.get_full_path())
        log.save()
