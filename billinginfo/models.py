from django.db import models
from users.models import Users

# Create your models here.
class Billinginfo(models.Model):
    # Add this back...
    #user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    nameoncard = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    cardnumber = models.CharField(max_length=20, blank=True, null=True)
    expdate = models.CharField(max_length=5, blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billinginfo'
