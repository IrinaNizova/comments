from django.db import models

class Comments(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
