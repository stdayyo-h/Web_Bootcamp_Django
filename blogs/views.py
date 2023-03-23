from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Blog


@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        data = {'blogs': list(blogs.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        blog = Blog(title=title, body=body)
        blog.save()
        data = {'message': 'Blog created successfully!'}
        return JsonResponse(data)


@csrf_exempt
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        data = {'error': 'Blog does not exist'}
        return JsonResponse(data, status=404)

    if request.method == 'GET':
        data = {'blog': {'title': blog.title, 'body': blog.body}}
        return JsonResponse(data)
    elif request.method == 'PUT':
        title = request.POST.get('title')
        body = request.POST.get('body')
        blog.title = title or blog.title
        blog.body = body or blog.body
        blog.save()
        data = {'message': 'Blog updated successfully!'}
        return JsonResponse(data)
    elif request.method == 'DELETE':
        blog.delete()
        data = {'message': 'Blog deleted successfully!'}
        return JsonResponse(data)
