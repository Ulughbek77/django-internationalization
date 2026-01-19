from django.db import models


class Item(models.Model):
    name = models.CharField()
    content = models.TextField()

