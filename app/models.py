from django.db import models

# Create your models here.
class Site(models.Model):
    SiteName=models.CharField(max_length=100)
    Cluster=models.CharField(max_length=100)
    Sector=models.CharField(max_length=100)
    CellName=models.CharField(max_length=100)
    Band=models.CharField(max_length=100)
    AntennaHeight=models.CharField(max_length=10)
    Azimuth=models.CharField(max_length=10)

    def __str__(self):
        return self.CellName