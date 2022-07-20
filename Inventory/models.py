from django.db import models
from User.models import User
from Product.models import Product
# Create your models here.

class Inventory(models.Model):
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    ModifiyBy = models.ForeignKey(User,on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,on_delete=models.CASCADE)
    IsDeleted = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

        def __str__(self):
             return self.pk