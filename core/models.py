from django.db import models

class Film(models.Model):
    title = models.CharField(max_length= 32)
    opis = models.TextField(max_length= 120)

