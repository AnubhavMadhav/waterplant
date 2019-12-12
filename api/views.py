from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Customers
from .serializers import CustomersSerializer


class ListCustomersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
