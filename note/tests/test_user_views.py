# text models
import json

import pytest

from note.models import Note
from user.models import UserDetails
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


# @pytest.mark.django_db
# def test_create_user_and_notes():
#     user = UserDetails.objects.create_user(username='mahesh', password='mahesh123', email='mahesh@gmail.com',
#                                            phone_number='3635667', location='bhimavaram')
#     assert user.username != 'santhosh'
class TestNotes:

    @pytest.mark.django_db
    def test_create_user(self, client):
        user_data = {"username": "robertdowney", "password": "779982", "email": "robert7799@gmail.com",
                     "phone_number": 779985, "location": "hydrabad"
                     }
        url = reverse("Registration")
        response = client.post(url, user_data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_to_get_notes(self, client):
        url = reverse("notes")
        user = UserDetails.objects.create_user(username="mahesh", password="mahesh123", email="mahesh123@gmail.com",
                                               phone_number="23456", location="bhimavaram")
        note = Note.objects.create(title="python", description="trending language", user_id=user)
        note_data = {"user_id": user.id}
        response = client.get(url, note_data)
        assert response.status_code == 201
        assert len(response.data.get("data")) == 1

    # @pytest.mark.abc
    @pytest.mark.django_db
    def test_to_delete_a_existed_note(self, client):
        # creating user

        user = UserDetails.objects.create_user(username="mahesh", password="mahesh123", email="mahesh123@gmail.com",
                                               phone_number="23456", location="bhimavaram", is_verified=True)

        # adding notes

        note = Note.objects.create(title="python", description="trending language", user_id=user)
        url = reverse("notes")

        # deleting existing note

        data = {"id": note.id}
        response = client.delete(url, data, content_type="application/json")
        assert response.status_code == 204
