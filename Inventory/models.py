from django.db import models
from User.models import User
from Product.models import Product
# Create your models here.
#
class Inventory(models.Model):
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey(User,related_name='Inventory_CreatedBy',on_delete=models.CASCADE)
    ModifiyBy = models.ForeignKey(User,related_name='Inventory_ModifiyBy',on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,related_name='Inventory_DeleteBy',on_delete=models.CASCADE)
    IsDeleted = models.BooleanField(default=True)
    Quality = models.IntegerField()
    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

        def __str__(self):
             return self.pk