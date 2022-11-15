from django.db import models
from product.models import Product
from user.models import User



class Orders(models.Model):
    o_id = models.AutoField(primary_key=True)
    p = models.ForeignKey(Product, to_field='p_id', on_delete=models.CASCADE)
    r = models.ForeignKey(User, to_field='r_id', on_delete=models.CASCADE)
    # r_id = models.IntegerField()
    # p_id = models.IntegerField()
    quantity = models.CharField(max_length=10)
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'orders'









