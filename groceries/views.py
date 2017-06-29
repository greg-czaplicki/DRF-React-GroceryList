from rest_framework.viewsets import ModelViewSet

from .models import Grocery
from .serializers import GrocerySerializer


# Create your views here.
class GroceryViewSet(ModelViewSet):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
