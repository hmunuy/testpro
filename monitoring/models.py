from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(default=0)
    insert_time = models.CharField(max_length=200)

