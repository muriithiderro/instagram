from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField(default="empty bio")
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True,default='default.jpg')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    
    @property
    def return_image(self):
        return self.photo.url
