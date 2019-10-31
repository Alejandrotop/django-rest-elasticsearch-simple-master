from rest_framework import serializers

from store.models import Store, Product

class StoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = ('title', )

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('title', 'store')