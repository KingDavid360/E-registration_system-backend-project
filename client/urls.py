from django.urls import path
from . import views

urlpatterns = [
    path('register-client/', views.register_client),
    path('fetch-course/', views.fetch_course),
]
