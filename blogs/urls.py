from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
    path('blogs/<int:id>/', BlogDetailAPIView.as_view(), name='blog-detail'),
]
