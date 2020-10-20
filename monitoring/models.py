from django.db import models


# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    insert_time = models.CharField(max_length=200)

class Host_report(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    insert_time = models.CharField(max_length=200)

class snmp_data(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface_snmp = models.CharField(max_length=200)
    status_snmp = models.CharField(max_length=200)

class snmp_data_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface_snmp = models.CharField(max_length=200)
    status_snmp = models.CharField(max_length=200)
    
    
class hostname(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    cpu_temp = models.IntegerField()
    ram_process = models.IntegerField()

class hostname_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    cpu_temp = models.IntegerField()
    ram_process = models.IntegerField()


class snmp_ap(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    numuser_wlc = models.IntegerField()
    insert_time = models.CharField(max_length=200)

class snmp_ap_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    numuser_wlc = models.IntegerField()
    insert_time = models.CharField(max_length=200)







