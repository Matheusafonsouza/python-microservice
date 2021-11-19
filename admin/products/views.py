from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from products.models import Product, User
from products.serializers import ProductSerializer, UserSerializer
from products.producer import publish


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        super().destroy(request, pk=pk)
        publish('product_deleted', pk)
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
