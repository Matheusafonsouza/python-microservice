from products.views import ProductViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('products', ProductViewSet)

urlpatterns = [] + router.urls
