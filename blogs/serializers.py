from rest_framework import serializers
from .models import Blog,Author


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=('__all__')
        # depth=2

       
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=('__all__')        