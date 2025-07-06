from rest_framework import serializers
from store.models import Product, ProductFeature
from account.models import StoreUser
from orders.models import Order


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


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreUser
        fields = ('phone', 'first_name', 'last_name', 'email', 'address', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        user = StoreUser(phone=validated_data['phone'], first_name=validated_data['first_name'],
                         last_name=validated_data['last_name'], email=validated_data['email'],
                         address=validated_data['address'])

        user.set_password(validated_data['password'])
        user.save()
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
