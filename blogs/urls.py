from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView,BlogFilterView,BlogSortView

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
    path('blogs/<int:id>/', BlogDetailAPIView.as_view(), name='blog-detail'),
    path('blogs/<str:author_name>/', BlogFilterView.as_view(), name='blog-filter'),
    path('blog/latest/', BlogSortView.as_view(), name='blog-sort'),
]
