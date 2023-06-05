from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.TextField()
    league = models.IntegerField()
    cup = models.IntegerField()
    concacaf = models.IntegerField()
    age = models.IntegerField()
    stadium = models.TextField(blank=True)
    state = models.TextField(blank=True)
    country = models.TextField(blank=True)
    nameleague = models.TextField(blank=True)
    image = models.TextField(blank=True)