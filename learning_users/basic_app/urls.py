from django.urls import path
from django.contrib import admin
from . import views

#for template tagging
app_name = 'basic_app'
urlpatterns = [
    path('basic_app/', views.register, name='register'),
    path('login/', views.user_login, name = 'user_login'),
]
