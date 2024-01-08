from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Treasure(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    treasures = models.ManyToManyField('Treasure', related_name='owners', blank=True)

    def __str__(self):
        return self.user_id.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)
            