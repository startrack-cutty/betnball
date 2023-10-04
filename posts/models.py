from django.db import models
from users.models import Users

# Create your models here.
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    # Add this line back
    #user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'