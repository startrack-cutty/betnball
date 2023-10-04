from django.db import models
from teams.models import Teams


# Create your models here.
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