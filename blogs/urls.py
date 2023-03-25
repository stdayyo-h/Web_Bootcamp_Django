
from django.urls import path
from .views import blog_view, blog_delete_view, blog_edit_view

urlpatterns = [
    path('blog/all', blog_view, name='blog_view'),
    path('blog/delete/<int:id>/', blog_delete_view, name='blog_delete_view'),
    path('blog/edit/', blog_edit_view, name='blog_edit_view'),
]