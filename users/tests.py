from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TestUser(APITestCase):
    """
    Test User model and API endpoints
    """

    def setUp(self) -> None:
        self.username = "test"
        self.password = "1234"
        self.email = "test@test.com"
        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
        )

    def test_create_user_success(self):
        """create user with valid data"""
        username = "test2"
        password = "1234"
        user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        self.assertEqual(user.username, username)
        self.assertNotEqual(user.password, password)

    def test_create_user_duplicate_username_failure(self):
        """create user with duplicated username"""
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                _ = get_user_model().objects.create_user(
                    username=self.username,
                    password=self.password
                )

        count = get_user_model().objects.filter(username=self.username).count()
        self.assertEqual(count, 1)

    def test_set_email_to_user_success(self):
        """set email field in user model"""
        email = "test@test.com"
        self.user.email = email
        self.user.save()

        self.assertEqual(self.user.email, email)

    def test_set_phone_number_to_user_success(self):
        """set phone number in user model"""
        phone_number = "09059528767"
        self.user.phone_number = phone_number
        self.user.save()

        self.assertEqual(self.user.phone_number, phone_number)

    def test_login_with_correct_credentials_success(self):
        """login with correct username and password"""
        username = self.username
        password = self.password
        url = reverse_lazy('v1:login')
        payload = {
            'username': username,
            'password': password
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_login_with_incorrect_credentials_failure(self):
        """login with incorrect username and password"""
        username = self.username
        password = "invalid_password"
        url = reverse_lazy('v1:login')
        payload = {
            'username': username,
            'password': password
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("refresh", response.data)
        self.assertNotIn("access", response.data)

    def test_valid_refresh_token_validation_success(self):
        """check valid refresh token"""
        token = RefreshToken.for_user(self.user)
        url = reverse_lazy("v1:refresh")
        payload = {"refresh": str(token)}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_invalid_refresh_token_validation_failure(self):
        """check invalid refresh token"""
        token = "invalid_token"
        url = reverse_lazy("v1:refresh")
        payload = {"refresh": token}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("refresh", response.data)
        self.assertNotIn("access", response.data)

    def test_user_profile_detail_success(self):
        pass

    def test_user_profile_detail_unauthorized_failure(self):
        pass

    def test_user_register_valid_data_success(self):
        pass

    def test_user_register_username_duplicate_failure(self):
        pass

    def test_user_register_phone_number_pattern_invalid_failure(self):
        pass

    def test_user_register_email_pattern_invalid_failure(self):
        pass

    def test_user_register_first_name_pattern_invalid_failure(self):
        pass

    def test_user_register_last_name_pattern_invalid_failure(self):
        pass

    def test_user_register_password_hashed(self):
        pass

    def test_confirm_user_email_success(self):
        pass

    def test_confirm_user_email_invalid_token_failure(self):
        pass

    def test_confirm_user_phone_number_success(self):
        pass

    def test_confirm_user_phone_number_invalid_token_failure(self):
        pass

    def test_user_edit_profile_success(self):
        pass

    def test_user_edit_profile_invalid_email_failure(self):
        pass

    def test_user_edit_profile_email_changed_confirm_email_switched(self):
        pass

    def test_user_edit_profile_invalid_phone_number_failure(self):
        pass

    def test_user_edit_profile_phone_number_changed_confirm_phone_number_switched(self):
        pass

    def test_user_edit_profile_invalid_first_name_failure(self):
        pass

    def test_user_edit_profile_invalid_last_name_failure(self):
        pass

    def test_user_logout_success(self):
        pass


