from django.db.backends.utils import logger
from rest_framework.response import Response
from user.utils import EncodeDecodeToken


#
# def verify_token(function):
#     def wrapper(self, request):
#         # if 'HTTP_AUTHORIZATION' not in request.META:
#         #     response = Response({'message': 'Token not provided in the header'})
#         #     response.status_code = 400
#         #     logger.info('Token not provided in the header')
#         #     return response
#         # token = request.META["HTTP_AUTHORIZATION"]
#         # user_id = EncodeDecodeToken.decode_the_token(token)
#         # request.data.update({'user_id': user_id.get('user_id')})
#         return function(self, request)
#
#     return wrapper
def verify_token(function):
    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get('Token')
        decode_the_token = EncodeDecodeToken.decode_the_token(token)
        user_id = decode_the_token.get('user_id')
        # user_list = UserDetails.objects.filter(pk=user_id)
        if not user_id:
            raise Exception('user not found')
        request.data.update({'user_id': user_id})
        return function(self, request, *args, **kwargs)

    return wrapper
