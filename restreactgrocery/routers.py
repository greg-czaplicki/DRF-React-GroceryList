from rest_framework import routers

from groceries.views import GroceryViewSet

router = routers.SimpleRouter()
router.register(r'groceries', GroceryViewSet)
