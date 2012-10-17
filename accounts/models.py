from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True)
    nickname = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile(user=user, nickname=user.username).save()
