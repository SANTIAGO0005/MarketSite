from django.db import models
from User.models import User
from Sales.models import Tax


# Create your models here.
class CategoryProduct(models.Model):
    """Model definition for CategoryProduct."""

    NameCategory = models.CharField( max_length=50)

    class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Category'

            def __str__(self):
                return self.pk+self.NameCategory
class Product(models.Model):
    """Model definition for Product."""
    
    CodeP = models.CharField(max_length=50)
    NameP = models.CharField(max_length=50)
    CategoryId = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    AmoutMin = models.IntegerField()
    AmountMax = models.IntegerField()
    Price = models.IntegerField()
    Cost = models.IntegerField()
    Taxid = models.ForeignKey(Tax, on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey(User,related_name='Product_CreatedBy',on_delete=models.CASCADE)
    ModifiyBy = models.ForeignKey(User,related_name='Product_ModifiyBy',on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,related_name='Product_DeleteBy',on_delete=models.CASCADE)
    IsDeleted = models.BooleanField(default=True)
    CreateAt = models.DateField(auto_now=False, auto_now_add=False)
    ModifiedAt = models.DateField(auto_now=False, auto_now_add=False)
    DeletedAt = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
            verbose_name = 'product'
            verbose_name_plural = 'products'


            def __str__(self):
                return self.pk+self.NameP
        


        
