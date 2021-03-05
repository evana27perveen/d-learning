from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PostModel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    content = models.TextField()
    blog_image = models.ImageField(upload_to='PostModel')
    datenow = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postman')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profile_page')
        

