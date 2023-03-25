from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    
    def __str__(self) -> str:
        return self.email


class Blog(models.Model):
    TECHNICAL = 'TC'
    LIFESTYLE = 'LF'
    SPORTS = 'SP'
    FOOD = 'FD'
    CATEGORY_CHOICES = [
        (TECHNICAL, 'Technical'),
        (LIFESTYLE, 'Lifestyle'),
        (SPORTS, 'Sports'),
        (FOOD, 'Food'),
    ]
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=False)
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=10000)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TECHNICAL)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=False)

    def __str__(self) -> str:
        return self.title