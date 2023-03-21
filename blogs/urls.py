from django.urls import path,include
from .views import BlogView

urlpatterns=[
    path('all/',BlogView.as_view())
]