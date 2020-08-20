from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Film(models.Model):
    title = models.CharField(max_length= 32)
    opis = models.TextField(max_length= 120)

#(class User(models.Model):
   # username = models.CharField(max_length= 32)
    #password = models.CharField(max_length= 32)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kawrgs):
    if created:
        Token.objects.create(user=instance)