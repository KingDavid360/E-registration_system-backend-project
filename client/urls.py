from django.urls import path
from . import views

urlpatterns = [
    path('register-client/', views.register_client),
]
