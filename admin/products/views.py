from rest_framework.viewsets import ModelViewSet
from products.models import Product, User
from products.serializers import ProductSerializer, UserSerializer
from products.producer import publish


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        publish()
        return super().list(request)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
