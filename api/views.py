from django.shortcuts import render
from rest_framework import generics, views, viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

from store.models import Product
from account.models import StoreUser
from .serializers import ProductSerializer, StoreUserSerializer, UserRegistrationSerializer


# Create your views here.


# we have product view set so we don't need these :)
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class StoreUserListAPIView(views.APIView):
    permission_classes = [IsAuthenticated]  # سطح دسترسی به api ها را  نشان میدهد
    authentication_classes = [BasicAuthentication]  # username and pass is needed only, نوع احراز هویت را نشان میدهد

    def get(self, request, *args, **kwargs):
        users = StoreUser.objects.all()
        serializer = StoreUserSerializer(users, many=True)
        return Response(serializer.data)


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = StoreUser.objects.all()
    serializer_class = UserRegistrationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['GET'], url_path='all_discount_products', url_name='all_discount_products',
            permission_classes=[AllowAny], authentication_classes=[BasicAuthentication])
    def discount_products(self, request):
        min_discount = request.query_params.get('min_discount', 0)
        try:
            min_discount = int(min_discount)
        except ValueError:
            return Response({'error': 'Invalid value for min discount'}, status=status.HTTP_400_BAD_REQUEST)
        products = self.queryset.filter(off__gt=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
