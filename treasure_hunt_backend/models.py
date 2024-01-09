from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Treasure(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(null=False)
    lng = models.FloatField(null=False)
    collected_by = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    treasures = models.ManyToManyField('Treasure', related_name='owners', blank=True)

    @property
    def treasure_count(self) -> int:
         return self.treasures.count()

    def __str__(self):
        return self.user_id.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)
