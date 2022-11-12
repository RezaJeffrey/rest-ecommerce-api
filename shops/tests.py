from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class TestShop(APITestCase):
    def set_up(self):
        self.username = 'test'
        self.password = '1234'
        self.email = 'test@test.com'
        self.role = 'sl'
        self.user = get_user_model().objects.create(
            username=self.username,
            password=self.password,
            email=self.email,
            role=self.role
        )

    def test_register_a_shop(self):
        pass

    def test_customer_register_a_shop(self):
        pass

    def test_duplicated_shops(self):
        pass

    def test_list_shops(self):
        pass

    def test_retrieve_shop(self):
        pass

    def test_update_shop(self):
        pass








