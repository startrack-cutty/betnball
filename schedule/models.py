from django.db import models
from teams.models import Teams
from sports.models import Sports

# Create your models here.
class Schedule(models.Model):
    # Add these lines back
    #away = models.ForeignKey('Teams', models.DO_NOTHING, db_column='away', blank=True, null=True)
    #home = models.ForeignKey('Teams', models.DO_NOTHING, db_column='home', related_name='schedule_home_set', blank=True, null=True)
    dateofgame = models.DateTimeField(db_column='dateOfGame', blank=True, null=True)  # Field name made lowercase.
    gameid = models.AutoField(db_column='gameID', primary_key=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    homescore = models.IntegerField(blank=True, null=True)
    awayscore = models.IntegerField(blank=True, null=True)
    quarter = models.CharField(max_length=45, blank=True, null=True)
    period = models.CharField(max_length=3, blank=True, null=True)
    half = models.CharField(max_length=3, blank=True, null=True)
    inning = models.IntegerField(blank=True, null=True)
    starttime = models.CharField(max_length=45, blank=True, null=True)
    # Add this line back
    # sport = models.ForeignKey('Sports', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'
