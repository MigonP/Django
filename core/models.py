from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Category(models.Model):
    GAMES = {
        (0,'Unknown'),
        (1,'World of Warcraft'),
        (2,'Conter-Strike'),
        (3,'League of Legends')
    }
    type = models.IntegerField(choices=GAMES, default=0)


    def __str__(self):
        return self.nasza_nazwa()
    def nasza_nazwa(self):
        return str(self.type)


class Film(models.Model):
    title = models.CharField(max_length= 32)
    opis = models.TextField(max_length= 120)
    category = models.OneToOneField(Category, on_delete=models.CASCADE,
                                    null=True,blank=True)

    def __str__(self):
        return str(self.title)



class Rate(models.Model):
    com = models.TextField(default='')
    star = models.IntegerField(default=10)
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             related_name='rate')



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kawrgs):
    if created:
        Token.objects.create(user=instance)


