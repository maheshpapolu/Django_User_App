from abc import ABC

from rest_framework import serializers
from user.models import UserDetails

import user


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    create a class named as user details and given attributes
    """

    class Meta:
        model = UserDetails
        fields = ['id', 'username', 'password', 'email', 'phone_number', 'location']

    def create(self, validated_data):
        return UserDetails.objects.create_user(**validated_data)
    # username = serializers.CharField(max_length=200)
    # password = serializers.CharField(max_length=20, write_only=True)
    # email = serializers.CharField(max_length=20)
    # phone_number = serializers.IntegerField()
    # location = serializers.CharField(max_length=20)
    # is_verified = serializers.BooleanField(default=False)
    # # token = serializers.CharField(max_length=200, required=False)
    #
    # def create(self, validated_data):
    #     return UserDetails.objects.create_user(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.location = validated_data.get('location', instance.location)
    #     # instance.token = validated_data.get('token', instance.token)
    #     instance.save()
    #     return instance
