from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from store.models import Product
from account.models import StoreUser
from .serializers import ProductSerializer, StoreUserSerializer, UserRegistrationSerializer


# Create your views here.


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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
