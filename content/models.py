from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Photo, self).save(*args, **kwargs)

    @classmethod
    def search(cls,query):
        Q = models.Q
        photos = Photo.objects.filter(Q(title__contains=query.lower())|Q(description__contains=query.lower()))
        return photos


class Comment(models.Model):
    photo = models.ForeignKey(Photo, related_name='comments')
    name = models.ForeignKey(User,related_name='user_comments')
    body = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.created)

