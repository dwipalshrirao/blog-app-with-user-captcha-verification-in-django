from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="images/blogs")

    choice=(
        ('public','public'),
        ('private','private')
    )
    status=models.CharField(choices=choice,max_length=20,null=True,blank=True)    
    created_date=models.DateTimeField(auto_now_add=True)
