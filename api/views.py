from django.shortcuts import render
from rest_framework import generics
from store.models import Product
from serializers import ProductSerializer


# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
