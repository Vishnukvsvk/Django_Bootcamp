from django.db import models

# Create your models here.


class Profile(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
