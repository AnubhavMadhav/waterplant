from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Customers
from .serializers import CustomersSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_customer(name="", cust_id=""):
        if name != "" and cust_id != "":
            Customers.objects.create(name=name, cust_id=cust_id)

    def setUp(self):
        # add test data
        self.create_customer("Anubhav Madhav", 1)
        self.create_customer("Digant Goyal", 2)
        self.create_customer("Deep Shah", 3)
        self.create_customer("Sasi", 4)


class GetAllCustomerTest(BaseViewTest):

    def test_get_all_customers(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("customers-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Customers.objects.all()
        serialized = CustomersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)