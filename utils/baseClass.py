# from User.models import User
# from django.db import models

# class BaseModel(models):
#     CreatedBy = models.ForeignKey(User,on_delete=models.CASCADE)
#     ModifieBy = models.ForeignKey(User,on_delete=models.CASCADE)
#     DeleteBy =  models.ForeignKey(User,on_delete=models.CASCADE)
#     IsDeleted = models.BooleanField(default=True)
#     CreateAt = models.DateField(auto_now=False, auto_now_add=False)
#     ModifiedAt = models.DateField(auto_now=False, auto_now_add=False)
#     DeletedAt = models.DateField(auto_now=False, auto_now_add=False)