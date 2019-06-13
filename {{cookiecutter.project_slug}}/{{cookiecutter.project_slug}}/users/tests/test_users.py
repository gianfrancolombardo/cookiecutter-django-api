""" User tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

# Model
from {{cookiecutter.project_slug}}.users.models import User

class UserAPITestCase(APITestCase):
    """ Users API test case. """

    def setUp(self):
        self.url = '/users/'
        self.data_base = {
            "email": "base@test.com",
            "username": "base",
            "password": "123456.a",
            "first_name": "test",
            "last_name": "test",
            "is_verified": True
        }
        User.objects.create_user(**self.data_base)
        self.data = {
            "email": "test@test.com",
            "username": "test",
            "password": "123456.a",
            "password_confirmation": "123456.a",
            "first_name": "test",
            "last_name": "test"
        }
        self.data_error = {
            "email": "test2@test.com",
            "username": "test2",
            "password": "123456.a",
            "password_confirmation": "123456.a"
        }
        self.data_error_code = {
            "token": "INCORECT"
        }
        self.data_login = {
            "email":"base@test.com",
            "password": "123456.a"
        }
        
        

    def test_signup_response_success(self):
        """ Create new user and expected successful response. """
        url = self.url + "signup/"
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_signup_response_error(self):
        """ Create new user without any field and expected error response. """
        url = self.url + "signup/"
        request = self.client.post(url, self.data_error)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verificate_account_response_error(self):
        """ Try to validate account with incorrect code and expected error response. """
        url = self.url + "verify/"
        request = self.client.post(url, self.data_error_code)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_response_success(self):
        """ Try to login account and expected success responce. """
        url = self.url + "login/"
        request = self.client.post(url, self.data_login)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_login_response_error(self):
        """ Try to login nonexistent account and expected error responce. """
        url = self.url + "login/"
        self.data_login["email"] = 'nonexistent@test.com'
        request = self.client.post(url, self.data_login)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)