from rest_framework import serializers
from .models import Customers


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("name", "cust_id")
