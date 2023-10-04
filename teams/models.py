from django.db import models
from sports.models import Sports

# Create your models here.
class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    sport = models.ForeignKey(Sports, models.DO_NOTHING, blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'