from django.template.defaulttags import url
from django.urls import path, re_path
from .views import BaseListView, CategoryDetailView, ProductDetailView, \
     search,search_page

urlpatterns = [
    path('', BaseListView.as_view(), name='main_page'),
    path('category/<slug:category_slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(),name='product_detail'),
    path('search/', search, name='search'),
    path('search_page/', search_page,name='search_page')
]
