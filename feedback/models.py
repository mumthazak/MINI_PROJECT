from django.db import models
from user.models import User
# Create your models here.

class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=30)
    r_id = models.IntegerField()
    # r=models.ForeignKey(User,to_field='r_id' ,on_delete=models.CASCADE)

    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'

