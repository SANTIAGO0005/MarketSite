from django.db import models
from django.contrib.auth.models import  AbstractUser,Group

# Create your models here.

class User(AbstractUser):
    """Model definition for User."""

    # TODO: Define fields here
    groups=models.ForeignKey(Group,on_delete=models.CASCADE)
    email=models.EmailField( max_length=50,unique=True)
    image =models.ImageField( upload_to='images/user', height_field=None, width_field=None, max_length=None)
    
    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        """Meta definition for User."""

        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username


# class Groupid(models.Model):
#     id = models.IntegerField()
#     groupName = models.CharField(max_length=50)

#     class meta:
#         verbose_name = 'Groupid'
#         verbose_name_plural = 'Groups'

#     def __str__(self):
#         """Unicode representation of Nave."""
#         return'{}'.format(self.id,self.groupName)


class Bussines(models.Model):
    """Model definition for Bussines."""
    name =models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Bussines'
        verbose_name_plural = 'Bussines'
        

    def __str__(self):
            return self.pk+self.namep

   

   