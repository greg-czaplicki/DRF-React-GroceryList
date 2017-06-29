from rest_framework.serializers import ModelSerializer

from groceries.models import Grocery


class GrocerySerializer(ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'

