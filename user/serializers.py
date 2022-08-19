from abc import ABC

from rest_framework import serializers
from user.models import UserDetails

import user


class UserDetailsSerializer(serializers.Serializer):
    """
    create a class named as user details and given attributes
    """
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=20, write_only=True)
    email = serializers.CharField(max_length=20)
    phone_number = serializers.IntegerField()
    location = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return UserDetails.objects.create_user(**validated_data)
