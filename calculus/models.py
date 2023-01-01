from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductPayment(models.Model):

    buyer = models.ForeignKey(User , on_delete=models.PROTECT , null=False)
    for_who = models.ForeignKey(User , on_delete=models.PROTECT , null=False,related_name='for_who')
    product_name = models.CharField(max_length=100)
    price = models.BigIntegerField(null=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.buyer} bought {self.product_name} for {self.for_who} and the price is {self.price}'