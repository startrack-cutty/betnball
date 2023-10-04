from django.db import models

# Create your models here.
class Pools(models.Model):
    poolid = models.AutoField(db_column='poolID', primary_key=True)  # Field name made lowercase.
    # Put back in
    # sport = models.ForeignKey('Sports', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(unique=True, max_length=45, blank=True, null=True)
    # Put back in
    # owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner', blank=True, null=True)
    buyin = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pools'
        db_table_comment = '\t\t\t\t\t'