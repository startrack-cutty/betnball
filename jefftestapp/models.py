from django.db import models

# Create your models here.
class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


# CRUD Operations
# create
# read
# update
# delete


