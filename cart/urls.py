from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('add_qty/<int:product_id>/', views.add_quantity,name='change_qty'),
    path('subtraction_quantity/<int:product_id>/',views.subtraction_quantity,name='subtraction_quantity')
]