from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    year = models.IntegerField(default=2000)
