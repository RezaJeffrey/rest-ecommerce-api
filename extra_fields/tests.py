from rest_framework.test import (
    APITestCase, APIRequestFactory,
    force_authenticate
)
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from products.models import Product


class TestExtra_Field(APITestCase):
    """
    Test Extra Field App and APIE endpoints
    """
    def setUp(self):
        self.username = 'test'
        self.password = '1234'
        self.email = 'test@test.com'
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )

    def test_create_extra_field(self):
        """
        create extra field with valid data by an authenticated user
        """
        pass



