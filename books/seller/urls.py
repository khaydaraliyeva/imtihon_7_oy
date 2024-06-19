from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='seller-index'),
    path('seller-products/', views.product_list, name='seller-product_list'),
    path('seller-products/create/', views.create_product, name='seller-create_product'),
    path('seller-products/<int:pk>/', views.product_detail, name='seller-product_detail'),
    path('seller-products/<int:pk>/edit/', views.update_product, name='seller-update_product'),
    path('seller-products/<int:pk>/delete/', views.delete_product, name='seller-delete_product'),

    path('seller-product_images/', views.product_image_list, name='seller-product_image_list'),
    path('seller-product_images/create/', views.create_product_image, name='seller-create_product_image'),
    path('seller-product_images/<int:pk>/', views.product_image_detail, name='seller-product_image_detail'),
    path('seller-product_images/<int:pk>/edit/', views.update_product_image, name='seller-update_product_image'),
    path('seller-product_images/<int:pk>/delete/', views.delete_product_image, name='seller-delete_product_image'),

    path('seller-product_videos/', views.product_video_list, name='seller-product_video_list'),
    path('seller-product_videos/create/', views.create_product_video, name='seller-create_product_video'),
    path('seller-product_videos/<int:pk>/', views.product_video_detail, name='seller-product_video_detail'),
    path('seller-product_videos/<int:pk>/edit/', views.update_product_video, name='seller-update_product_video'),
    path('seller-product_videos/<int:pk>/delete/', views.delete_product_video, name='seller-delete_product_video'),
]
