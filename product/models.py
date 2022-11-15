from django.db import models

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=15)
    image = models.CharField(max_length=15)
    description = models.CharField(max_length=30)
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


