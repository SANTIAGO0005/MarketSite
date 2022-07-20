from django.db import models
from User.models import Bussines
from User.models import User

# Create your models here.

class Invoice(models.Model):
    """Model definition for Invoice."""

    InvoiceNumber = models.CharField(max_length=50)
    EnterpriceId = models.ForeignKey(Bussines, on_delete=models.CASCADE)
    TaxId =  models.ForeignKey("Sales.Tax", on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    ModifieBy = models.ForeignKey(User,on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,on_delete=models.CASCADE)
    IsDeleted = models.BooleanField(default=True)
    CreateAt = models.DateField(auto_now=False, auto_now_add=False)
    ModifiedAt = models.DateField(auto_now=False, auto_now_add=False)
    DeletedAt = models.DateField(auto_now=False, auto_now_add=False)
    InvoiceDate = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoice"

    def __str__(self):
        return self.pk



class InvoiceDetails(models.Model):
    """Model definition for InvoiceDetails."""

    CodeP = models.CharField(max_length=50)
    Desc =  models.CharField(max_length=50)
    Quality =  models.IntegerField()
    PriceP = models.IntegerField()
    CostP = models.IntegerField()
    UnitP =  models.CharField(max_length=50)
    InvoiceId = models.ForeignKey("Sales.Invoice", on_delete=models.CASCADE)
    Precentage = models.IntegerField()
    PencetagePrice = models.IntegerField()
    Total = models.IntegerField()

    class Meta:
        verbose_name = "InvoiceDetails"
        verbose_name_plural = "InvoiceDetails"

    def __str__(self):
        return self.pk

    


class Tax(models.Model):
    """Model definition for Tax."""

    desc=  models.CharField( max_length=50)
    percentage = models.IntegerField()

    class Meta:
        verbose_name = "tax"
        verbose_name_plural = "tax"

    def __str__(self):
        return self.pk+self.desc+self.percentage

    



 