from django.urls import path
from . import views

urlpatterns = [
    path('login-admin/', views.login_admin),
    path('fetch-clients/', views.fetch_clients),
]
