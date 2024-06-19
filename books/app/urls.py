from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register', views.register, name="user_register"),
    path('logout', views.user_logout, name="user_logout"),
]
