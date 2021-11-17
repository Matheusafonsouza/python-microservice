from products.views import ProductViewSet, UserViewSet
from rest_framework import routers


router = routers.SimpleRouter()

router.register('products', ProductViewSet)
router.register('users', UserViewSet)

urlpatterns = [] + router.urls
