from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    "verbose plural name"
    class Meta:
        verbose_name_plural = 'Posts'

