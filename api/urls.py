from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('products', views.ProductViewSet)
urlpatterns = [
    # path('products/', views.ProductListAPIView.as_view(), name='products_list_api'),
    # path('product/<pk>', views.ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('users/', views.StoreUserListAPIView.as_view(), name='users_list_api'),
    path('register/', views.UserRegistrationAPIView.as_view(), name='register_api'),
    path('', include(router.urls))
]
