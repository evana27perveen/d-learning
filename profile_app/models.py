from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class ProfileAddOnModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='malik')
    my_bio = models.CharField(max_length=100, blank=False, null=True)
    profile_image = models.ImageField(upload_to='ProfileAddOnModel', default='static/image/dflt_user.png')
    cover_image = models.ImageField(upload_to='ProfileAddOnModel', default='static/image/dflt_cover.png')

    def __str__(self):
        return self.my_bio

    def get_absolute_url(self):
        return reverse('profile_page')



