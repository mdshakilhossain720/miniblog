from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=150)
    des=models.TextField()
    def __str__(self):
        return self.title
    
