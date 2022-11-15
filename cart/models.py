from django.db import models
from product.models import Product
# Create your models here.
class Cart(models.Model):
    c_id = models.AutoField(primary_key=True)
    # status = models.CharField(max_length=15)
    r_id = models.IntegerField()
    p=models.ForeignKey(Product,to_field='p_id',on_delete=models.CASCADE)
    # p_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'
