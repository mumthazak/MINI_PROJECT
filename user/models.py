from django.db import models



class User(models.Model):
    r_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'





