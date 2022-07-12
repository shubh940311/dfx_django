from unicodedata import name
from django.urls import path
from .views import success,hotel_image_view

urlpatterns = [
    path('image_upload/', hotel_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
]