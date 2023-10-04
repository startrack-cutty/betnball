from django.db import models

# Create your models here.
class Sports(models.Model):
    sport_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'sports'