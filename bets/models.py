from django.db import models
from users.models import Users
from schedule.models import Schedule
from teams.models import Teams


# Create your models here.
class Bets(models.Model):
    bet_id = models.BigAutoField(primary_key=True)
    # Add back in
    #user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    #opponent = models.ForeignKey('Users', models.DO_NOTHING, db_column='opponent', related_name='bets_opponent_set', blank=True, null=True)
    #game = models.ForeignKey('Schedule', models.DO_NOTHING, blank=True, null=True)
    # Add back in...
    #userteamchoice = models.ForeignKey('Teams', models.DO_NOTHING, db_column='userteamchoice', blank=True, null=True)
    betamount = models.FloatField(db_column='betAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bets'