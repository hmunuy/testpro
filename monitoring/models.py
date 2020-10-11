from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    insert_time = models.CharField(max_length=200)

class snmp_data(models.Model):
    hostname = models.CharField(max_length=200)
    interface_snmp = models.CharField(max_length=200)
    status_snmp = models.CharField(max_length=200)
    
