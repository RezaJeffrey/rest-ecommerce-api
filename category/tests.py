from rest_framework.test import APITestCase
from django.urls import reverse
from category.models import Category


class TestCategory(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.parent = Category.objects.create(
            name="parentTestName",
            parent=None,
        )
        cls.category = Category.objects.create(
            name="categoryNameTest",
            parent=cls.parent  # pycharm unresolved error(test is runing well I have no Idea:))
        )  # TODO ask mehran for static files test

    def test_category_model_name_success(self):
        self.assertEqual(self.category.name, "categoryNameTest")

    def test_category_model_name_failure(self):
        self.assertNotEqual(self.category.name, "wrong_name")

    def test_category_model_string(self):
        self.assertEqual(str(self.category), "categoryNameTest")

    def test_category_model_parent_name(self):
        self.assertEqual(self.category.parent.name, "parentTestName")

    def test_category_model_parents_parent(self):
        self.assertEqual(self.category.parent.parent, None)