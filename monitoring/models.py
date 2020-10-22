from django.db import models


# Create your models here.
#Show on Wwb Page  DEVIE UP TIME
class Host(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    insert_time = models.CharField(max_length=200)
#Report
class Host_report(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    insert_time = models.CharField(max_length=200)
#Show on Wwb Page Interface
class snmp_data(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface_snmp = models.CharField(max_length=200)
    status_snmp = models.CharField(max_length=200)
#Report
class snmp_data_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface_snmp = models.CharField(max_length=200)
    status_snmp = models.CharField(max_length=200)
    
    #Show on Wwb Page HOST NAME CPU RAM 
class hostname(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    cpu_temp = models.IntegerField()
    ram_process = models.IntegerField()
#Report
class hostname_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    cpu_temp = models.IntegerField()
    ram_process = models.IntegerField()

#Show on Wwb Page CLIENT ON PAGE 
class snmp_ap(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    numuser_wlc = models.IntegerField()
    insert_time = models.CharField(max_length=200)
#Report
class snmp_ap_report(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    numuser_wlc = models.IntegerField()
    insert_time = models.CharField(max_length=200)

#Show on Wwb Page IP MAC CLIENT 
class snmp_ap_ipmac(models.Model):
    ip_hostname = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

#Show on Wwb Page IN OUT BOUND  
class in_out(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface_in_out = models.CharField(max_length=200)
    interface_in = models.CharField(max_length=200)
    interface_out = models.CharField(max_length=200)





