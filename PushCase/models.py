from django.db import models

# Create your models here.

class Pushcase(models.Model):
    """Model definition for Pushcase."""

    PushcaseNumeber = models.CharField(max_length=50)
    EnterpriceId = models.ForeignKey(Bussines, on_delete=models.CASCADE)
    CreatedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    ModifieBy = models.ForeignKey(User,on_delete=models.CASCADE)
    DeleteBy =  models.ForeignKey(User,on_delete=models.CASCADE)
    IsDeleted = models.BooleanField(default=True)
    CreateAt = models.DateField(auto_now=False, auto_now_add=False)
    ModifiedAt = models.DateField(auto_now=False, auto_now_add=False)
    DeletedAt = models.DateField(auto_now=False, auto_now_add=False)
    PushcaseDate = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Pushcase"
        verbose_name_plural = "Pushcase"

    def __str__(self):
        return self.pk


class PushcaseDetail(models.Model):
    """Model definition for PushcaseDetail."""

    CodeP = models.CharField(max_length=50)
    Desc =  models.CharField(max_length=50)
    Quality =  models.IntegerField()
    PriceP = models.IntegerField()
    CostP = models.IntegerField()
    UnitP =  models.CharField(max_length=50)
    PushcaseId = models.ForeignKey("Sales.Invoice", on_delete=models.CASCADE)
    Precentage = models.IntegerField()
    PencetagePrice = models.IntegerField()
    Total = models.IntegerField()

    class Meta:
        verbose_name = "PushcaseDetail"
        verbose_name_plural = "PushcaseDetails"

    def __str__(self):
        return self.pk