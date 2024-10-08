# Док: https://www.w3schools.com/django/django_urls.php

from django.urls import path
from . import views
from .views import TeacherLoginView, ProtectedTeacherView
from .authadmin import AdminLoginView, ProtectedAdminView

urlpatterns = [
    # path('auth/', views.auth), # @Mansur Добавляем эндпоинт авторизации. Просто к примеру. 
    # path('login/', views.login), # @Mansur Добавляем эндпоинт авторизации. Просто к примеру. 
    path('teacher/', TeacherLoginView.as_view(), name='teacher_login'),
    path('testing/', ProtectedTeacherView.as_view(), name='protected_teacher'),
    path('adminPanel/', AdminLoginView.as_view(), name='admin_login'),
    path('get/', ProtectedAdminView.as_view(), name='get_admin'),
]