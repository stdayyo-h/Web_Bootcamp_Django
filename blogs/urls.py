from django.urls import path,include
from .views import blog_view,blog_delete_view

urlpatterns=[
    path('all/',blog_view),
    path('delete/',blog_delete_view)
]