from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    password=models.CharField(max_length=200,null=True)
    company_name=models.CharField(max_length=200,null=True)
    company_type=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name