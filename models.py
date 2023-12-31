# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bets(models.Model):
    bet_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    opponent = models.ForeignKey('Users', models.DO_NOTHING, db_column='opponent', related_name='bets_opponent_set', blank=True, null=True)
    game = models.ForeignKey('Schedule', models.DO_NOTHING, blank=True, null=True)
    userteamchoice = models.ForeignKey('Teams', models.DO_NOTHING, db_column='userteamchoice', blank=True, null=True)
    betamount = models.FloatField(db_column='betAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bets'


class Billinginfo(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    nameoncard = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    cardnumber = models.CharField(max_length=20, blank=True, null=True)
    expdate = models.CharField(max_length=5, blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billinginfo'


class Footballteams(models.Model):
    sport = models.ForeignKey('Sports', models.DO_NOTHING, blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'footballteams'


class Picks(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    poolid = models.ForeignKey('Pools', models.DO_NOTHING, db_column='poolID', blank=True, null=True)  # Field name made lowercase.
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





class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Schedule(models.Model):
    away = models.ForeignKey('Teams', models.DO_NOTHING, db_column='away', blank=True, null=True)
    home = models.ForeignKey('Teams', models.DO_NOTHING, db_column='home', related_name='schedule_home_set', blank=True, null=True)
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
    sport = models.ForeignKey('Sports', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Sports(models.Model):
    sport_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'sports'


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


class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)  # The composite primary key (user_id, username) found, that is not supported. The first column is selected.
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    favorite_team = models.ForeignKey(Teams, models.DO_NOTHING, db_column='favorite_team', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('user_id', 'username'),)
