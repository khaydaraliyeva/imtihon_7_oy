from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin-index'),
    path('dashboard', views.dashboard, name='admin-dashboard'),
    path('admin-user_profile_list/', views.user_profile_list, name='admin-user_profile_list'),
    path('admin-user_profiles/create/', views.create_user_profile, name='admin-create_user_profile'),
    path('admin-user_profiles/<int:pk>/', views.user_profile_detail, name='admin-user_profile_detail'),
    path('admin-user_profiles/<int:pk>/edit/', views.update_user_profile, name='admin-update_user_profile'),
    path('admin-user_profiles/<int:pk>/delete/', views.delete_user_profile, name='admin-delete_user_profile'),

    path('admin-categories_list', views.category_list, name='admin-category_list'),
    path('admin-categories/create/', views.create_category, name='admin-create_category'),
    path('admin-categories/<int:pk>/', views.category_detail, name='admin-category_detail'),
    path('admin-categories/<int:pk>/edit/', views.update_category, name='admin-update_category'),
    path('admin-categories/<int:pk>/delete/', views.delete_category, name='admin-delete_category'),

    path('admin-products/', views.product_list, name='admin-product_list'),
    path('admin-products/create/', views.create_product, name='admin-create_product'),
    path('admin-products/<int:pk>/', views.product_detail, name='admin-product_detail'),
    path('admin-products/<int:pk>/edit/', views.update_product, name='admin-update_product'),
    path('admin-products/<int:pk>/delete/', views.delete_product, name='admin-delete_product'),

    path('admin-product_images/', views.product_image_list, name='admin-product_image_list'),
    path('admin-product_images/create/', views.create_product_image, name='admin-create_product_image'),
    path('admin-product_images/<int:pk>/', views.product_image_detail, name='admin-product_image_detail'),
    path('admin-product_images/<int:pk>/edit/', views.update_product_image, name='admin-update_product_image'),
    path('admin-product_images/<int:pk>/delete/', views.delete_product_image, name='admin-delete_product_image'),

    path('admin-product_videos/', views.product_video_list, name='admin-product_video_list'),
    path('admin-product_videos/create/', views.create_product_video, name='admin-create_product_video'),
    path('admin-product_videos/<int:pk>/', views.product_video_detail, name='admin-product_video_detail'),
    path('admin-product_videos/<int:pk>/edit/', views.update_product_video, name='admin-update_product_video'),
    path('admin-product_videos/<int:pk>/delete/', views.delete_product_video, name='admin-delete_product_video'),

    path('admin-carts/', views.cart_list, name='admin-cart_list'),
    path('admin-carts/create/', views.create_cart, name='admin-create_cart'),
    path('admin-carts/<int:pk>/', views.cart_detail, name='admin-cart_detail'),
    path('admin-carts/<int:pk>/edit/', views.update_cart, name='admin-update_cart'),
    path('admin-carts/<int:pk>/delete/', views.delete_cart, name='admin-delete_cart'),

    path('admin-cart_products/', views.cart_product_list, name='admin-cart_product_list'),
    path('admin-cart_products/create/', views.create_cart_product, name='admin-create_cart_product'),
    path('admin-cart_products/<int:pk>/', views.cart_product_detail, name='admin-cart_product_detail'),
    path('admin-cart_products/<int:pk>/edit/', views.update_cart_product, name='admin-update_cart_product'),
    path('admin-cart_products/<int:pk>/delete/', views.delete_cart_product, name='admin-delete_cart_product'),

    path('admin-comments/', views.comment_list, name='admin-comment_list'),
    path('admin-comments/create/', views.create_comment, name='admin-create_comment'),
    path('admin-comments/<int:pk>/', views.comment_detail, name='admin-comment_detail'),
    path('admin-comments/<int:pk>/edit/', views.update_comment, name='admin-update_comment'),
    path('admin-comments/<int:pk>/delete/', views.delete_comment, name='admin-delete_comment'),


]
