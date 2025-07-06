from rest_framework import serializers
from store.models import Product, ProductFeature
from account.models import StoreUser


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'new_price', 'features']


class StoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreUser
        fields = ['id', 'phone', 'first_name', 'last_name', 'email', 'address', 'is_staff', 'is_active']
