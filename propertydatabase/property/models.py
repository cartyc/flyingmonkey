from django.contrib.gis.db import models

# Create your models here.

class address(models.Model):

    number = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    streetType = models.CharField(max_length=20, null=True, blank=True)

    municipality = models.CharField(max_length=255, null=True, blank=True)

class mainParcel(models.Model):

    mainAddress = models.ForeignKey(address, null=True, blank=True)
    pin = models.CharField(max_length=9)
    roll = models.CharField(max_length=10, null=True, blank=True)

    geom = models.PointField(srid=4326, null=True)
    objects = models.GeoManager()


class subordParcel(models.Model):

    pin = models.ForeignKey(mainParcel)
