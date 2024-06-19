from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='client-index'),
    path('add_to_cart/<int:pk>', views.add_cart, name='add_cart'),
    path('book/', views.shop, name="client-shop"),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('checkout', views.chackout, name="client-checkout"),
    path('filter_by_category/<int:pk>', views.filter_by_category, name='filter_by_category'),
    path('filter_by_brand/<int:pk>', views.filter_by_brand, name='filter_by_brand'),
    path('filter_by_price/', views.filter_by_price, name='filter_by_price'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('liked-products/', views.liked_products, name='liked_products'),
    path('search/', views.search_products, name='search_products'),
    path('contact', views.contact, name='contact'),
    path('search_by_category/<int:pk>', views.search_by_category, name='search_by_category'),
]
