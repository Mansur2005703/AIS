# Док: https://www.w3schools.com/django/django_urls.php

from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth), # @Mansur Добавляем эндпоинт авторизации. Просто к примеру. 
    path('login/', views.login), # @Mansur Добавляем эндпоинт авторизации. Просто к примеру. 
]