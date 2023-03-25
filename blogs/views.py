from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def blog_view(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:
            blog = Blog.objects.filter(id=id).first()
            if not blog:
                return JsonResponse({"message": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
            serialized = BlogSerializer(blog)
            return JsonResponse({"data": serialized.data}, status=status.HTTP_200_OK)
        else:
            blogs = Blog.objects.all()
            serialized = BlogSerializer(blogs, many=True)
            return JsonResponse({"data": serialized.data}, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        serializer = BlogSerializer(data=json.loads(request.body))  
        if serializer.is_valid():  
            serializer.save()  
            return JsonResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)  
        else:  
            return JsonResponse({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    

@csrf_exempt
def blog_delete_view(request):
    if request.method == 'DELETE':
        id = request.GET.get('id')
        if id:
            blog = Blog.objects.filter(id=id).first()
            if not blog:
                return JsonResponse({"message": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
            blog.delete()
            return JsonResponse({"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({"message": "ID is required."}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def blog_edit_view(request):
    if request.method == 'PUT':
        request_body = json.loads(request.body)
        id = request_body.get('id')
        blog = Blog.objects.filter(id=id).first()
        if not blog:
            return JsonResponse({"message": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(blog, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
            