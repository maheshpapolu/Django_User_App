from http import client

from django.contrib.auth.models import User
from django.http import response
import pytest
import json
from django.urls import reverse
from note.models import Note


class TestNoteAPI:
    # Create user
    @pytest.mark.django_db
    def test_create_note(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='mahesh', password='122345', email='mahesh@gmail.com',
                                                     phone_number='783974', location='bhimavaram')
        url = reverse('Login')

        # login successful
        data = {'username': 'mahesh', 'password': '122345'}
        response = client.post(url, data)
        print(dir(response))
        json_data = json.loads(response.content)
        print(response.json())
        assert response.status_code == 200

        # Create notes
        url = reverse('notes')
        data = {'title': 'python', 'description': 'programing language', 'user_id': 1}
        response = client.post(url, data)
        json_data = json.loads(response.content)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_get_note(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='mahesh', password='122345', email='mahesh@gmail.com',
                                                     phone_number='783974', location='bhimavaram')

        # Create notes
        url = reverse('notes')
        data = {'title': 'python', 'description': 'programing language', 'user_id': user.id}
        response = client.post(url, data)
        json_data = json.loads(response.content)
        assert response.status_code == 201

        # get note
        url = reverse('notes')
        data = {'user_id': user.id}
        response = client.get(url, data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_update_note(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='mahesh', password='122345',
                                                     email='mahesh@gmail.com',
                                                     phone_number='783974', location='bhimavaram')

        # Create notes
        url = reverse('notes')
        data = {'title': 'python', 'description': 'programing language', 'user_id': user.id}
        response = client.post(url, data)
        note_id = response.data.get('data').get('id')
        assert response.status_code == 201

        # get note
        # we need note_id to update the data
        url = reverse('notes')
        data = {'title': 'django', 'description': 'framework', 'user_id': user.id, 'id': note_id}
        response = client.put(url, data, content_type='application/json')
        print(response.data)
        assert response.status_code == 202

    @pytest.mark.django_db
    def test_delete_note(self, client, django_user_model):
        user = django_user_model.objects.create_user(username='mahesh', password='122345', email='mahesh@gmail.com',
                                                     phone_number='783974', location='bhimavaram')

        # Create notes
        url = reverse('notes')
        data = {'title': 'python', 'description': 'programing language', 'user_id': user.id}
        response = client.post(url, data)
        note_id = response.data.get('data').get('id')
        assert response.status_code == 201

        # get note
        url = reverse('notes')
        data = {'id': note_id}
        response = client.delete(url, data, content_type='application/json')
        assert response.status_code == 204
