from django.db import models
from users.models import Users
#from pools.models import Pools

# Create your models here.
class Picks(models.Model):
    # Add back in...
    #userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    #poolid = models.ForeignKey('Pools', models.DO_NOTHING, db_column='poolID', blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    game1winner = models.IntegerField(blank=True, null=True)
    game2winner = models.IntegerField(blank=True, null=True)
    game3winner = models.IntegerField(blank=True, null=True)
    game4winner = models.IntegerField(blank=True, null=True)
    game5winner = models.IntegerField(blank=True, null=True)
    game6winner = models.IntegerField(blank=True, null=True)
    game7winner = models.IntegerField(blank=True, null=True)
    game8winner = models.IntegerField(blank=True, null=True)
    game9winner = models.IntegerField(blank=True, null=True)
    game10winner = models.IntegerField(blank=True, null=True)
    game11winner = models.IntegerField(blank=True, null=True)
    game12winner = models.IntegerField(blank=True, null=True)
    game13winner = models.IntegerField(blank=True, null=True)
    game14winner = models.IntegerField(blank=True, null=True)
    game15winner = models.IntegerField(blank=True, null=True)
    game16winner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picks'
