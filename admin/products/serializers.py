from rest_framework import serializers
from products.models import Product, User
from products.producer import publish
from django.forms.models import model_to_dict


class ProductSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        publish('product_created', model_to_dict(product))
        return product

    def update(self, instance, validated_data):
        instance = super(ProductSerializer, self).update(
            instance, validated_data)
        publish('product_updated', model_to_dict(instance))
        return instance

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
