""" Adding models for apple"""
from django.db import models


class Apple(models.Model):
    """class apple"""
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    photo_url = models.URLField()

    def __str__(self):
        return str(self.name)
