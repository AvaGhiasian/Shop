from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response

from store.models import Product
from account.models import StoreUser
from .serializers import ProductSerializer, StoreUserSerializer


# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreUserListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        users = StoreUser.objects.all()
        serializer = StoreUserSerializer(users, many=True)
        return Response(serializer.data)
