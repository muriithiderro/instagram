from django.db import models
from django.conf import settings
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField(default="empty bio")
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True,default='default.jpg')

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    
    @property
    def return_image(self):
        return self.photo.url

def post_save_user_model_receiver(sender, instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)