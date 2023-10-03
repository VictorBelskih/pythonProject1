from django.db import models
import osgeo
from django.db import connection
import json
from django.contrib.gis.db import models


class Gggg(models.Model):
    id_0 = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    farm_name = models.CharField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    fld_id = models.IntegerField(blank=True, null=True)
    flp_id = models.IntegerField(blank=True, null=True)
    f_id = models.IntegerField(blank=True, null=True)
    tlu = models.CharField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    geojson = models.TextField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.geojson

    class Meta:
        db_table = 'gggg'
