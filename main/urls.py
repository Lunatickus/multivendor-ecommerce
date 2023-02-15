from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('address', CustomerAddressViewSet)
router.register('productrating', ProductRatingViewSet)

urlpatterns = [
    path('vendors/', VendorList.as_view()),
    path('vendor/<int:pk>/', VendorDetail.as_view()),

    path('products/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),

    path('categories/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),

    path('customers/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerDetail.as_view()),

    path('orders/', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
]

urlpatterns += router.urls