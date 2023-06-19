from django.test import TestCase

from accounts.views import create_user

import request

# Create your tests here.


class TestViews(TestCase):
    def __init__(self):
        pass

    def test_create_user(self):
        data = {
            "username": "test000",
            "password": "password",
        }
        response = request.post(
            "http://localhost:8000/api/v1/accounts/signup/", data=data
        )

        assertEquals(response.status, 200)
