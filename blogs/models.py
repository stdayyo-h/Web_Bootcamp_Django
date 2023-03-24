from django.db import models

# Create your models here.
class Blog(models.Model):
    author_name = models.CharField(max_length=50,null=True,blank=False)
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=10000)