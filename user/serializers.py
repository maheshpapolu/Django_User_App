from abc import ABC

from rest_framework import serializers

import user


class UserDetailsSerializer(serializers.Serializer):
    """
    create a class named as user details and given attributes
    """
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=20)
    phone_number = serializers.IntegerField()
    location = serializers.CharField(max_length=20)
