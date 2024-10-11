from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
     path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("products/",views.getProducts,name="products"),
    path("products/<str:pk>/",views.getProduct,name="product"),
    path('user/register/',views.getRegisterUser,name='user-register'),
    path('user/orders/<str:pk>',views.getMyOrders,name='my-orders'),
    path('<str:pk>/pay/',views.updateOrderToPaid, name='user-order'),
    path('user/orders/<str:pk>/', views.getOrderById, name='user-order'),
    path('orders/add/',views.addOrderItems,name='orders-add'),
]