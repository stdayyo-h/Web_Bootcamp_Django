from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog
# Create your views here.


class BlogView(APIView):


    def get(self,request,*args,**kwargs):
        id=request.GET.get('id')
        if(id):
            blogs=Blog.objects.filter(id=id)
        else:
            blogs=Blog.objects.all()
        serialized=BlogSerializer(blogs,many=True)
        return Response({"status":"success","data":serialized.data},status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
    