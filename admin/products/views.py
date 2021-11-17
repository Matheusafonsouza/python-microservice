from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
