from rest_framework.test import APITestCase


class AddressTests(APITestCase):
    # post code can only be 10 digits 
    def test_invalid_post_code_len(self):
        pass

    # post code's first five digits should contain 0, 2, 5
    def test_invalid_post_code_format(self):
        pass

    def test_valid_post_code(self):
        pass

    def test_anonymous_user_can_not_access_to_url(self):
        pass

    def test_authenticated_user_can_access_to_url(self):
        pass

    def test_create_address_with_correct_payloads(self):
        pass

    def test_delete_address(self):
        pass

    def test_retrieve_address(self):
        pass

    def test_update_address(self):
        pass