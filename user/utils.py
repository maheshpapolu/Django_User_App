import jwt


class EncodeDecodeToken:
    @staticmethod
    def encode_the_token(payload):
        encoded_token = jwt.encode(payload, 'secret', algorithm='HS256')
        return encoded_token
    
    @staticmethod
    def decode_the_token(token):
        try:
            decoded_token = jwt.decode(token, 'secret', algorithms=['HS256'])
            return decoded_token
        except jwt.exceptions.InvalidTokenError:
            raise Exception('invalid token')
