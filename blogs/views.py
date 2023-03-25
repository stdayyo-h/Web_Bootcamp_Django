from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog,Author
from .serializers import BlogSerializer


class BlogListAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailAPIView(APIView):
    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogFilterView(APIView):
    def get(self, request, author_name):
        try:
            author = Author.objects.get(name=author_name)
        except Author.DoesNotExist:
            return Response({'error': 'Author not found.'}, status=status.HTTP_404_NOT_FOUND)

        blogs = Blog.objects.filter(author=author)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class BlogSortView(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('-created_at')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
