from user.utils import EncodeDecodeToken
import json
from .redis_service import RedisServer
import logging


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


class NoteCREDOperations:
    def __init__(self):

        self.cache_memory = RedisServer()

    def add_note(self, note, user_id):
        try:
            notes = self.get_note(user_id)
            note_id = note.get('id')
            notes.update({note_id: note})
            self.cache_memory.set(user_id, json.dumps(notes))
        except Exception as e:
            logging.error(e)

    def get_note(self, user_id):
        """
        getting note-data from the memory
        """
        try:
            cache_data = self.cache_memory.get(user_id)
            return {} if not cache_data else json.loads(cache_data)
        except Exception as e:
            logging.exception(e)

    def update_note(self, updated_note, user_id):
        """
        update the existing note in the memory
        """
        try:

            note_id = updated_note.get("id")
            note_dict = self.get_note(user_id)
            note_dict.update({note_id: updated_note})
            self.add_note(user_id=user_id, note=note_dict)
        except Exception as er:
            logging.exception(er)

    def delete_note(self, user_id, note_id):
        """
        deleting the note from the memory
        """
        try:
            note_dict = self.get_note(user_id)
            if note_dict.get(note_id):
                note_dict.pop(note_id)
                self.add_note(user_id=user_id, note=note_dict)
        except Exception as error:
            logging.exception(error)
