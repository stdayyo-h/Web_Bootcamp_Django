from django.urls import path,include
from .views import BlogView

urlpatterns=[
    path('home/',BlogView.as_view())
]