from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


# class BlogView(APIView):


#     def get(self,request,*args,**kwargs):
#         id=request.GET.get('id')
#         if(id):
#             blogs=Blog.objects.filter(id=id)
#         else:
#             blogs=Blog.objects.all()
#         serialized=BlogSerializer(blogs,many=True)
#         return Response({"status":"success","data":serialized.data},status=status.HTTP_200_OK)
    
    
#     def post(self, request):
#         serializer = BlogSerializer(data=request.data)  
#         if serializer.is_valid():  
#             serializer.save()  
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#         else:  
#             return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    
@csrf_exempt
def blog_view(request):
    # print(request.method)
    if(request.method=='GET'):
        id=request.GET.get('id')
        if(id):
            blogs=Blog.objects.filter(id=id)
        else:
            blogs=Blog.objects.all()
        serialized=BlogSerializer(blogs,many=True)
        return JsonResponse({"data":serialized.data},status=status.HTTP_200_OK)
        
    if(request.method=='POST'):
        serializer = BlogSerializer(data=json.loads(request.body))  
        if serializer.is_valid():  
            serializer.save()  
            return JsonResponse({"data":serializer.data},status=status.HTTP_200_OK)  
        else:  
            return JsonResponse({"data":serializer.data},status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def blog_delete_view(request):
    if(request.method=="GET"):
        id=request.GET.get('id')
        if(id):
            blog=Blog.objects.get(id=id)
            blog.delete()
            return JsonResponse({"message":"succesfully Deleted"},status=status.HTTP_202_ACCEPTED)
        else:
            return JsonResponse({"message":"Invalid Id"},status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def blog_edit_view(request):
    if(request.method=='POST'):
        requestbody=json.loads(request.body)
        if('id' in requestbody):
            blog=Blog.objects.filter(id=requestbody['id'])
        else:
            blog=NULL        
        if(blog):
            blog=blog[0]
            if('title' in requestbody):
                blog.title=requestbody['title']
            if('body' in requestbody):
                blog.body=requestbody['body']
            blog.save()
            return JsonResponse({"message":"succesfully Edited"},status=status.HTTP_202_ACCEPTED)
        else:
            return JsonResponse({"message":"Invalid Id"},status=status.HTTP_404_NOT_FOUND)